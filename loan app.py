import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Custom CSS for button styling
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color: #1F4E79;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        padding: 0.6rem 1rem;
    }

    div.stButton > button:first-child:hover {
        background-color: #163A5C;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# reset state this function resets the form to its default values when the reset button is clicked
def reset_form():
    st.session_state["customer_name"] =""
    st.session_state["sex"] = 1
    st.session_state["age"] = 30
    st.session_state["education"] = 1
    st.session_state["marriage"] = 1
    st.session_state["limit_bal"] = 50000.0

    st.session_state["pay_0"] = 0
    st.session_state["pay_2"] = 0
    st.session_state["pay_3"] = 0
    st.session_state["pay_4"] = 0
    st.session_state["pay_5"] = 0
    st.session_state["pay_6"] = 0

    st.session_state["bill_amt1"] = 0.0
    st.session_state["bill_amt2"] = 0.0
    st.session_state["bill_amt3"] = 0.0
    st.session_state["bill_amt4"] = 0.0
    st.session_state["bill_amt5"] = 0.0
    st.session_state["bill_amt6"] = 0.0

    st.session_state["pay_amt1"] = 0.0
    st.session_state["pay_amt2"] = 0.0
    st.session_state["pay_amt3"] = 0.0
    st.session_state["pay_amt4"] = 0.0
    st.session_state["pay_amt5"] = 0.0
    st.session_state["pay_amt6"] = 0.0


model = joblib.load("loan_default_model.pkl")
scaler = joblib.load("scaler.pkl")


# st.title("Customer Loan Default Risk Assessment")
st.markdown(
    '<h1 style="color:#1F4E79;">🛡️ Credora</h1>',
    unsafe_allow_html=True
)

st.write(
    "AI-powered loan default risk assessment using customer "
    "financial and demographic information."
)

st.info(
    "Enter the customer's information below, then click "
    "**Assess Loan Risk** to generate a risk assessment."
)
st.caption(
    "💡 Tip: Complete all relevant customer information for the most "
    "informative assessment."
)


st.divider()
# sex, education and marriage are categorical variables, we use selectbox to get the input from user
# st.subheader("👤 Customer Demographics")
st.markdown(
    '<h2 style="color:#1F4E79;">Customer Demographics</h2>',
    unsafe_allow_html=True
)

customer_name = st.text_input(
    "Customer Name",
    placeholder="Enter customer's name",
    key="customer_name"
)


col1, col2 = st.columns(2)# gives two spaces beside each other

with col1:
    sex = st.selectbox(
    "Sex",
    options=[1, 2],
    format_func=lambda x: "Male" if x == 1 else "Female",
    key ="sex"
    )
with col2:
    # age should be between 18 and 100
    if "age" not in st.session_state:
        st.session_state["age"] = 30 #age should be at 30 by default even when it's not set in the session state

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        key="age"
    )


col3, col4 = st.columns(2)
with col3:
    education = st.selectbox(
    "Education",
    options=[1, 2, 3, 4],
    format_func=lambda x: {
        1: "Graduate School",
        2: "University",
        3: "High School",
        4: "Others"
    }[x],
    key="education" 
    )
with col4:
    marriage = st.selectbox(
    "Marital Status",
    options=[0, 1, 2, 3],
    format_func=lambda x: {
        0: "Others",
        1: "Married",
        2: "Single",
        3: "Others"
    }[x],
    key="marriage"
    )


# st.subheader("💳 Credit Limit")

st.markdown(
    '<h2 style="color:#1F4E79;"> Credit Limit</h2>',
    unsafe_allow_html=True
)

limit_bal = st.number_input(
    "Credit Limit",
    min_value=0.0,
    value=50000.0,
    step = 1000.0,
    help="The customer's assigned credit limit",
    key="limit_bal"
)



# st.subheader("💰 Billing & Payment Information")
st.markdown(
    '<h2 style="color:#1F4E79;">Billing & Payment Information</h2>',
    unsafe_allow_html=True
)


# creating and expander for the billing and payment information section
with st.expander("Enter 6-Month Billing & Payment History"):
    # Payment Delay
    st.subheader("Payment Delay For The Previous Payments")
    col1, col2, col3 = st.columns(3)
    with col1:
        pay_0 = st.number_input(
            "Most Recent Payment Delay",
             min_value=0,
             value=0,
             help="Number of months the customer delayed on their most recentpayment",
             key="pay_0"
        )
    with col2:
        pay_2 = st.number_input(
            "Payment Delay - Month 2",
            value=0,
            help="Number of months the customer delayed on their payment",
            key="pay_2"
        )   
    with col3:
        pay_3 = st.number_input(
            "Payment Delay - Month 3", 
            min_value=0,
            value=0,
            help="Number of months the customer delayed on their payment",
            key="pay_3"
        )

    col4, col5, col6 = st.columns(3)
    with col4:
        pay_4 = st.number_input(
            "Payment Delay - Month 4",
            min_value=0,
            value=0,
            help="Number of months the customer delayed on their payment",
            key="pay_4"
        )
    with col5:
        pay_5 = st.number_input(
            "Payment Delay - Month 5",
            min_value=0,
            value=0,
            help="Number of months the customer delayed on their payment",
            key="pay_5"
        )
    with col6:
        pay_6 = st.number_input(
            "Payment Delay - Month 6",
            min_value=0,
            value=0,    
            help="Number of months the customer delayed on their payment",
            key="pay_6"
        )

    # Monthly Amount Of Bill Statements For Previous 6 Months
    st.subheader("Monthly Amount Of Bill Statements For Previous 6 Months")
    st.caption("Enter the customer's bill statement amounts for each of the previous six months.")

    col1, col2, col3 = st.columns(3)
    with col1:
        bill_amt1 = st.number_input("Bill Amount - Month 1", min_value=0.0,
                                     value=0.0, key="bill_amt1")

    with col2:
        bill_amt2 = st.number_input("Bill Amount - Month 2", min_value=0.0, value=0.0, key="bill_amt2")
    with col3:
        bill_amt3 = st.number_input("Bill Amount - Month 3", min_value=0.0, value=0.0, key="bill_amt3")

    col4, col5, col6 = st.columns(3)
    with col4:
        bill_amt4 = st.number_input("Bill Amount - Month 4", min_value=0.0, value=0.0, key="bill_amt4")
    with col5:
        bill_amt5 = st.number_input("Bill Amount - Month 5", min_value=0.0, value=0.0, key="bill_amt5")
    with col6:
        bill_amt6 = st.number_input("Bill Amount - Month 6", min_value=0.0, value=0.0, key="bill_amt6")

    # Monthly Amount Of Previous Payments For Previous 6 Months 
    st.subheader("Monthly Amount Of Previous Payments For Previous 6 Months")
    st.caption("Enter the amounts the customer paid during each of the previous six months.")

    col1, col2, col3 = st.columns(3)
    with col1:
        pay_amt1 = st.number_input("Payment Amount - Month 1", min_value=0.0, value=0.0, key="pay_amt1")
    with col2:
        pay_amt2 = st.number_input("Payment Amount - Month 2", min_value=0.0, value=0.0, key="pay_amt2")
    with col3:
        pay_amt3 = st.number_input("Payment Amount - Month 3", min_value=0.0, value=0.0, key="pay_amt3")

    col4, col5, col6 = st.columns(3)
    with col4:
        pay_amt4 = st.number_input("Payment Amount - Month 4", min_value=0.0, value=0.0, key="pay_amt4")
    with col5:
        pay_amt5 = st.number_input("Payment Amount - Month 5", min_value=0.0, value=0.0, key="pay_amt5")
    with col6:
        pay_amt6 = st.number_input("Payment Amount - Month 6", min_value=0.0, value=0.0, key="pay_amt6")

#let's calculate the engineered features(average payment delay, average bill amount and average payment amount)
# maximum payment delay in months
max_pay_delay = max(
    pay_0, pay_2, pay_3,
    pay_4, pay_5, pay_6
)

# average bill payment amount
avg_bill_amt = (
    bill_amt1 + bill_amt2 + bill_amt3 +
    bill_amt4 + bill_amt5 + bill_amt6
) / 6

# average payment amount
avg_pay_amt = (
    pay_amt1 + pay_amt2 + pay_amt3 +
    pay_amt4 + pay_amt5 + pay_amt6
) / 6


input_data = pd.DataFrame({
    "LIMIT_BAL": [limit_bal],
    "AGE": [age],
    "SEX": [sex],
    "EDUCATION": [education],
    "MARRIAGE": [marriage],
    "MAX_PAY_DELAY": [max_pay_delay],
    "AVG_BILL_AMT": [avg_bill_amt],
    "AVG_PAY_AMT": [avg_pay_amt]
})

# One-hot encode categorical variables
input_data = pd.get_dummies(
    input_data,
    columns=["SEX", "EDUCATION", "MARRIAGE"],
    dtype=int
)

# Reindex the input data to match the training data columns
input_data = input_data.reindex(
    columns=scaler.feature_names_in_,
    fill_value=0
)

# Ensure that the input data has the same columns as the training data
scaled_input = scaler.transform(input_data)


# Loan Assessment Section
st.divider()
# st.subheader("Loan Risk Assessment")
st.markdown(
    '<h2 style="color:#1F4E79;">Loan Risk Assessment Result</h2>',
    unsafe_allow_html=True
)

# this is for adding a rest button to the form
button_col1, button_col2 = st.columns(2)
with button_col1:
    st.button(
        "🗘 Reset",
        on_click=reset_form,
        use_container_width=True,
        key ="clear_button"
    )

with button_col2:
    assess_button = st.button(
        "Assess Loan Risk",
        use_container_width = True,
        key="assess_button"
    )
if assess_button:
    prediction = model.predict(scaled_input)

    st.divider()
    # st.subheader("Customer Loan Risk Assessment Summary")
    st.markdown(
    '<h2 style="color:#1F4E79;">Customer Assessment Summary</h2>',
    unsafe_allow_html=True
    )

    if prediction[0] == 1:
        st.error( "⚠️ The model predicts a higher likelihood of loan default.")
    else:
        st.success("✅ The model predicts a lower likelihood of loan default.")

    probability = model.predict_proba(scaled_input)[0][1]  # Probability of default
    if probability < 0.30:
        risk_level = "Low Risk"
    elif probability < 0.60:
        risk_level = "Medium Risk"
    else:
        risk_level = "High Risk"

    result1, result2 = st.columns(2)
    with result1:
        if risk_level == "Low Risk":
            st.success(f"🟢 {risk_level}")
        elif risk_level == "Medium Risk":
            st.warning(f"🟡 {risk_level}")
        else:
            st.error(f"🔴 {risk_level}")

    with result2:
        st.metric("Probability of default", f"{probability: .1%}")
    # INTERPRETATION: the model estimates a {probability} probability that this customer belongs to the (default/non-default class)

    st.progress(probability) #this creates a visual bar to make probability easier to interpret at a glace
    st.caption(
    "Risk classification: Low Risk < 30% | "
    "Medium Risk 30–59% | High Risk ≥ 60%"
    )

    # Customer Assessment Summary Section

    summary_data = {
        "Feature": [
            "Customer Name",
            "Credit Limit",
            "Age",
            "Maximum Payment Delay",
            "Average Bill Amount",
            "Average Payment Amount"
        ],
        "Value":[
            customer_name,
            f"${limit_bal:,.2f}",
            age,
            max_pay_delay,
            f"${avg_bill_amt:,.2f}",
            f"${avg_pay_amt:,.2f}"
        ]
    }
    st.table(summary_data)

     # Explanation of the assessment summary
    # st.subheader(" What This Result Means Is That:")
    st.markdown(
    '<h2 style="color:#1F4E79;">💡 What This Result Means</h2>',
    unsafe_allow_html=True
    )

    if risk_level == "Low Risk":
        st.write(
            "The customer has a relatively low predicted probability of default. "
            "Based on the information provided, the customer appears less likely to default."
        )

    elif risk_level == "Medium Risk":
        st.write(
            "The customer has a moderate predicted probability of default. "
            "The application may require additional review before making a lending decision."
        )

    else:
        st.write(
            "The customer has a high predicted probability of default. "
            "The application should be reviewed carefully before making a lending decision."
        )

    st.divider()

    # st.subheader(" Model Performance")
    st.markdown(
    '<h2 style="color:#1F4E79;">Model Performance</h2>',
    unsafe_allow_html=True
    )

    st.write(
        "This loan risk assessment is powered by a Gradient Boosting Classifier "
        "trained using SMOTE to address class imbalance."
    )

    # to desplay the model performance metrics
    metric1, metric2, metric3 = st.columns(3)

    with metric1:
        st.metric("Accuracy", "74.8%")

    with metric2:
        st.metric("Precision", "44.5%")

    with metric3:
        st.metric("Recall", "60.9%")

    metric4, metric5 = st.columns(2)

    with metric4:
        st.metric("F1 Score", "51.4%")

    with metric5:
        st.metric("ROC-AUC", "69.8%")

    with st.expander("How the Model Works"):

        # explanation of how the model works    
        st.write(
            "The model uses customer demographic, credit, billing, and payment "
            "information to estimate the probability of loan default."
        )

        st.write(
            "**SMOTE:** The original dataset contained fewer customers who "
            "defaulted than customers who did not. SMOTE was used during training "
            "to help the model learn from the minority class."
        )

        st.write(
            "**Gradient Boosting:** Multiple decision trees are built sequentially, "
            "with each tree learning from the errors of the previous trees. "
            "The resulting model is then used to estimate the customer's default risk."
        )
    with st.expander("Key Features Influencing the Model"):

        st.write(
            "The following features had the greatest influence on the model's "
            "predictions during model evaluation:"
        )

        feature_data = {
            "Feature": [
                "Maximum Payment Delay",
                "Credit Limit",
                "Age",
                "Average Payment Amount",
                "Average Bill Amount"
            ],
            "Importance": [
                "55.85%",
                "25.56%",
                "7.28%",
                "5.51%",
                "4.65%"
            ]
        }
    st.table(feature_data)

    st.divider()

    # shows a disclaimer
    st.markdown(
        '<h3 style="color:#1F4E79;">⚠️ Responsible Use</h3>',
        unsafe_allow_html=True
    )

    st.caption(
        "This assessment is intended to support loan risk evaluation and "
        "should be used alongside other relevant customer and financial "
        "information. It should not be treated as the sole basis for lending decisions."
    )
    