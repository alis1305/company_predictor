import streamlit as st
import pandas as pd
from pycaret.classification import load_model, predict_model

# Load the trained model
model = load_model('model')

# Define the Streamlit app
def main():
    st.title("Company Success Prediction")

# User input for each feature
#company = st.text_input("Company Name")
    
# Get user input for industry using selectbox
    industry = st.selectbox("Industry",("Fintech", "Web3", "E-commerce", "Consumer Others","EdTech","ESG","Enterprise SaaS","Others"))
# Initialize all variables to 0
    fintech = web3 = ecommerce = consumer_others = edtech = esg = enterprise_saas = others = 0
# Set the corresponding variable to 1 based on industry choice
    if industry == "Fintech":
        fintech = 1
    elif industry == "Web3":
        web3 = 1
    elif industry == "E-commerce":
        ecommerce = 1
    elif industry == "Consumer Others":
        consumer_others = 1
    elif industry == "EdTech":
        edtech = 1
    elif industry == "ESG":
        esg = 1
    elif industry == "Enterprise SaaS":
        enterprise_saas = 1
    elif industry == "Others":
        others = 1       
        
# Get user input for business model using selectbox
    business_model = st.selectbox("Business Model",("B2B","B2C","B2B2C","Others"))
# Initialize business model encoded variable
    business_model_Encoded = -1  # Default value for an unrecognized model (Others)
# Set the corresponding variable based on business model choice
    if business_model == "B2B":
        business_model_Encoded = 0
    elif business_model == "B2C":
        business_model_Encoded = 2
    elif business_model == "B2B2C":
        business_model_Encoded = 1
    else:
        business_model_Encoded = -1  # "Others" category or any unrecognized category
   
# Get user input for country of headquarter using selectbox
    country = st.selectbox("Please select the country where your company is primarily based in",
    ["Australia","Indonesia","Malaysia","Philippines", "Singapore", "Thailand", "Vietnam", "Others"],)
# Set the corresponding variable to 1 based on country choice
    if country == "Australia":
        country_Encoded = 0
    elif country == "Indonesia":
        country_Encoded = 1
    elif country == "Malaysia":
        country_Encoded = 2
    elif country == "Philippines":
        country_Encoded = 3
    elif country == "Singapore":
        country_Encoded = 4
    elif country == "Thailand":
        country_Encoded = 5
    elif country == "Vietnam":
        country_Encoded = 6
    else:
        country_Encoded = -1  # "Others" category or any unrecognized category

#Get user input for total number of employees in the company
    glassdoor_total_employees = st.selectbox("Total Number of Employees in the Company", ("0 to 200", "201 to 500", "501 to 1000", "1001 to 5000", "5001 to 10000", "10000+"))
# Initialize glassdoor total employees encoded variable
    glassdoor_total_employees_Encoded = -1  # Default value for an unrecognized model (Others)
# Set the corresponding variable based on number of employees choice
    if glassdoor_total_employees == "10000+":
        glassdoor_total_employees_Encoded = 0
    elif glassdoor_total_employees == "1001 to 5000":
        glassdoor_total_employees_Encoded = 1
    elif glassdoor_total_employees == "201 to 500":
        glassdoor_total_employees_Encoded = 2
    elif glassdoor_total_employees == "5001 to 10000":
        glassdoor_total_employees_Encoded = 3
    elif glassdoor_total_employees == "501 to 1000":
        glassdoor_total_employees_Encoded = 4
    elif glassdoor_total_employees == "0 to 200":
        glassdoor_total_employees_Encoded = 5
    
# Get user input for Glassdoor rating and recommendation percentage using sliders
# Slider for rating between 0.0 and 5.0, default at 3.5
    #glassdoor_rating = st.slider("Glassdoor Rating", 0.0, 5.0, 3.5)
 # Slider for recommendation percentage between 0 and 100, default at 50    
    #glassdoor_recommend_percentage = st.slider("Glassdoor Recommend Percentage", 0, 100, 50)
        
# Get user input for similar business model overseas
#similar_businessmodel_overseas = st.selectbox("Similar Business Model Overseas", [0, 1])
    similar_businessmodel_overseas = st.selectbox("Is there a Similar Business Model Overseas?",("Yes", "No")) 
    if similar_businessmodel_overseas == "Yes":
        similar_businessmodel_overseas = 1
    else: # This will handle the case when the input is "No"
        similar_businessmodel_overseas = 0

# Get user input for patent holding
    patent = st.selectbox("Does your company currently hold any patents or is it in the process of obtaining one?", ("Yes", "No"))
    if patent == "Yes":
        patent = 1
    else: # This will handle the case when the input is "No"
        patent = 0

# Get user input if the company has pivoted from their original idea or direction
    pivot = st.selectbox("Has your company pivoted from its original idea or direction?", ("Yes", "No"))
    if pivot == "Yes":
        pivot = 1
    else: # This will handle the case when the input is "No"
        pivot = 0
    
# Get user input if the company is a subsidiary of another company or it is a corporate spinoff 
    subsidiary_corporatespinoff = st.selectbox("Is your company a subsidiary of another company or a result of a corporate spinoff?", ("Yes", "No"))
    if subsidiary_corporatespinoff == "Yes":
        subsidiary_corporatespinoff = 1 #company is a subsidiary or corporate spinoff 
    else: # This will handle the case when the input is "No"
        subsidiary_corporatespinoff = 0

# Get user input if the any of the team member is a repeat founder 
    firsttime_founder = st.selectbox("Is everyone on the founding team a first-time founder?", ("Yes", "No"))
    if firsttime_founder == "Yes":
        firsttime_founder = 1 # First-time founder
    else:
        firsttime_founder = 0 # Not First-time founder

# Get user input if the any of the team member has technical background    
    tech_founder = st.selectbox("Does any of your founders have a technical background?", ("Yes", "No"))
    if tech_founder == "Yes":
        tech_founder = 1 # the founding team has tech founder
    else:
        tech_founder = 0 # the founding team does not have any tech founder 

# Get user input for the founder's age when they started the company
    #foundersage_when_started = st.number_input("What was the founder's age when they started the company? If there is a team of founders, please provide the average age", min_value=20, max_value=75)
    
# Get user input if any member of the founding team graduated from overseas unversity 
    graduated_overseas_uni = st.selectbox("Has any member of your founding team graduated from a university outside your home country?", ("Yes", "No"))
    if graduated_overseas_uni == "Yes":
        graduated_overseas_uni = 1
    else:
        graduated_overseas_uni = 0

# Initialize variables for each university category
    aust_uni = china_uni = india_uni = sg_uni = sea_uni = us_uk_uni = no_graduate = 0

# Get user to select the country where the founding team graduated from
    university = st.multiselect("Select the country where your founders earned their university degrees (you may choose more than one)",
    ["Australia University", "China University", "India University", "Singapore University", 
     "University based in other Southeast Asia countries", "University based in Europe or US", 
     "Others or Did not graduate from university"])
    if "Australia University" in university:
        aust_uni = 1
    if "China University" in university:
        china_uni = 1
    if "India University" in university:
        india_uni = 1
    if "Singapore University" in university:
        sg_uni = 1
    if "University based in other Southeast Asia countries" in university:
        sea_uni = 1
    if "University based in Europe or US" in university:
        us_uk_uni = 1
    if "Others or Did not graduate from university" in university:
        no_graduate = 1


# Initialize variables for each investor category
    investor_500global = investor_alphajwc = investor_cyberagentcapital = investor_eastvc = investor_ggv = 0
    investor_insignia = investor_jungle = investor_openspace = investor_sequoia = investor_vertex = 0
    investor_wavemaker = investor_yc = investor_others = 0
# Get user to select the investor(s) that have invested in their company        
    investor = st.multiselect("Select the investor(s) that have invested in your company (you may choose more than one)",
    ["500 Global","Alpha JWC","Cyber Agent Capital","East Venture","Golden Gate Venture","Insignia","Jungle Venture","Openspace VC", "Sequoia","Vertex","Wavemaker", "Y Combinator", "Investor(s) not in the list"],)
    if "500 Global" in investor:
        investor_500global = 1
    if "Alpha JWC" in investor:
        investor_alphajwc = 1
    if "Cyber Agent Capital" in investor:
        investor_cyberagentcapital = 1
    if "East Venture" in investor:
        investor_eastvc = 1
    if "Golden Gate Venture" in investor:
        investor_ggv = 1
    if "Insignia" in investor:
        investor_insignia = 1
    if "Jungle Venture" in investor:
        investor_jungle = 1
    if "Openspace VC" in investor:
        investor_openspace = 1
    if "Sequoia" in investor:
        investor_sequoia = 1
    if "Vertex" in investor:
        investor_vertex = 1
    if "Wavemaker" in investor:
        investor_wavemaker = 1
    if "Y Combinator" in investor:
        investor_yc = 1
    if "Investor(s) not in the list" in investor:
        investor_others = 1

    sucessranking_four_gdranking = 0
    sucessranking_three_employees = 0
    valauation_divide_vdminusyf = 0
    sucessranking_two_valdivideyear = 0
    year_operating = 0
    years_to_unicorn = 0
    exit = 0
    foundersage_when_started = 0
    glassdoor_rating = 0
    glassdoor_recommend_percentage = 0

# Create a dictionary with the inputs
    input_data = {
        #'company': company,
        'fintech': fintech,
        'web3': web3,
        'ecommerce': ecommerce,
        'consumer_others': consumer_others,
        'edtech': edtech,
        'esg': esg,
        'enterprise_saas': enterprise_saas,
        'others': others,
        'business_model': business_model,
        'business_model_Encoded': business_model_Encoded,
        'glassdoor_rating': glassdoor_rating,
        'sucessranking_four_gdranking': sucessranking_four_gdranking,
        'glassdoor_total_employees': glassdoor_total_employees,
        'glassdoor_total_employees_Encoded': glassdoor_total_employees_Encoded,
        'sucessranking_three_employees': sucessranking_three_employees,
        'glassdoor_recommend_percentage': glassdoor_recommend_percentage,
        'valauation_divide_vdminusyf': valauation_divide_vdminusyf,
        'sucessranking_two_valdivideyear': sucessranking_two_valdivideyear,
        'similar_businessmodel_overseas': similar_businessmodel_overseas,
        'year_operating': year_operating,
        'years_to_unicorn': years_to_unicorn,
        'exit': exit,
        'country': country,
        'country_Encoded': country_Encoded,
        'patent': patent,
        'pivot': pivot,
        'subsidiary_corporatespinoff': subsidiary_corporatespinoff,
        'firsttime_founder': firsttime_founder,
        'tech_founder': tech_founder,
        'foundersage_when_started': foundersage_when_started,
        'graduated_overseas_uni': graduated_overseas_uni,
        'sg_uni': sg_uni,
        'india_uni': india_uni,
        'us_uk_uni': us_uk_uni,
        'sea_uni': sea_uni,
        'china_uni': china_uni,
        'aust_uni': aust_uni,
        'no_graduate': no_graduate,
        'investor_vertex': investor_vertex,
        'investor_500global': investor_500global,
        'investor_eastvc': investor_eastvc,
        'investor_sequoia': investor_sequoia,
        'investor_yc': investor_yc,
        'investor_insignia': investor_insignia,
        'investor_ggv': investor_ggv,
        'investor_wavemaker': investor_wavemaker,
        'investor_openspace': investor_openspace,
        'investor_alphajwc': investor_alphajwc,
        'investor_jungle': investor_jungle,
        'investor_cyberagentcapital': investor_cyberagentcapital,
        'investor_others': investor_others,
    }

    # Convert the dictionary to a DataFrame
    input_df = pd.DataFrame([input_data])

    # Make predictions
    if st.button("Predict"):
        prediction = predict_model(model, data=input_df)
        
        if int(prediction['prediction_label']) == 1:
            predicted_outcome = "High"
        else:
            predicted_outcome = "Low"            
        
        st.write("Predicted Startup Success is: ", predicted_outcome)

if __name__ == '__main__':
    main()
