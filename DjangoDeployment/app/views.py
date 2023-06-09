from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import getCustomerData
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Stores views of our django app. HTML / webpages are rendered from here.


def homePage(request):
    context = {}
    return render(request, 'app/home.html', context)


def predictPage(request):
    form = getCustomerData()
    print('before post method')
    if request.method == 'POST':
        print('just after post method')
        form = getCustomerData(request.POST)
        if form.is_valid():
            print('form is valid')
            CustomerID = form.cleaned_data['CustomerID']
            Count = form.cleaned_data['Count']
            Country = form.cleaned_data['Country']
            State = form.cleaned_data['State']
            City = form.cleaned_data['City']
            ZipCode = form.cleaned_data['ZipCode']
            Latitude = form.cleaned_data['Latitude']
            Longitude = form.cleaned_data['Longitude']
            Gender = form.cleaned_data['Gender']
            SeniorCitizen = form.cleaned_data['SeniorCitizen']
            Partner = form.cleaned_data['Partner']
            Dependents = form.cleaned_data['Dependents']
            TenureMonths = form.cleaned_data['TenureMonths']
            PhoneService = form.cleaned_data['PhoneService']
            MultipleLines = form.cleaned_data['MultipleLines']
            InternetService = form.cleaned_data['InternetService']
            OnlineSecurity = form.cleaned_data['OnlineSecurity']
            OnlineBackup = form.cleaned_data['OnlineBackup']
            DeviceProtection = form.cleaned_data['DeviceProtection']
            TechSupport = form.cleaned_data['TechSupport']
            StreamingTV = form.cleaned_data['StreamingTV']
            StreamingMovies = form.cleaned_data['StreamingMovies']
            Contract = form.cleaned_data['Contract']
            PaperlessBilling = form.cleaned_data['PaperlessBilling']
            PaymentMethod = form.cleaned_data['PaymentMethod']
            MonthlyCharges = form.cleaned_data['MonthlyCharges']
            TotalCharges = form.cleaned_data['TotalCharges']
            CLTVs = form.cleaned_data['CLTV']
            input_data = get_input_data(CustomerID, Count, Country, State, City, ZipCode, Latitude, Longitude, Gender, SeniorCitizen, Partner, Dependents, TenureMonths, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges, CLTVs)
            transformed_input = transform_input(input_data)
            # print(input_data)
            print(transformed_input)
            # form.save()
            print('form saved')



            # Loading the model
            with open('../artifacts/models/AdaBoost.pkl', 'rb') as file:
                model = pickle.load(file)


            prediction = model.predict(transformed_input)
            print(prediction)
            context_result = {'churn':prediction}
            return redirect(request, 'app/result.html', context_result)
    context = {'form':form}
    return render(request, "app/predict.html", context)




def get_input_data(CustomerID, Count, Country, State, City, ZipCode, Latitude, Longitude, Gender, SeniorCitizen, Partner, Dependents, TenureMonths, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges, CLTVs):
    input_data = pd.DataFrame({
        'CustomerID' : CustomerID,
        'Count' : Count,
        'Country' : Country,
        'State' : State,
        'City' : City,
        'Zip Code' : ZipCode,
        'Latitude' : Latitude,
        'Longitude' : Longitude,
        'Gender' : Gender,
        'Senior Citizen' : SeniorCitizen,
        'Partner' : Partner,
        'Dependents' : Dependents,
        'Tenure Months' : TenureMonths,
        'Phone Service' : PhoneService,
        'Multiple Lines' : MultipleLines,
        'Internet Service' : InternetService,
        'Online Security' : OnlineSecurity,
        'Online Backup' : OnlineBackup,
        'Device Protection' : DeviceProtection,
        'Tech Support' : TechSupport,
        'Streaming TV' : StreamingTV,
        'Streaming Movies' : StreamingMovies,
        'Contract' : Contract,
        'Paperless Billing' : PaperlessBilling,
        'Payment Method' : PaymentMethod,
        'Monthly Charges' : MonthlyCharges,
        'Total Charges' : TotalCharges,
        'CLTV' : CLTVs
    }, index=[0])


    return input_data




def transform_input(data):
    categorical_features = [
        'Gender', 'Senior Citizen', 'Partner', 'Dependents', 'Phone Service', 'Multiple Lines',
        'Internet Service', 'Online Security', 'Online Backup', 'Device Protection', 'Tech Support',
        'Streaming TV', 'Streaming Movies', 'Contract','Paperless Billing', 'Payment Method'
    ]

    dummy_features = [
        'Gender', 'Senior Citizen', 'Partner', 'Dependents', 'Phone Service', 'Multiple Lines',
        'Internet Service','Online Security', 'Online Backup', 'Device Protection', 'Tech Support', 
        'Streaming TV', 'Streaming Movies', 'Contract','Paperless Billing', 'Payment Method'
    ]

    drop_features = [
        'CustomerID', 'Country', 'State', 'City', 'Zip Code', 'Count'
    ]

    data_new = data.drop(drop_features, axis=1)
    print(data_new)
    label_enc = LabelEncoder()
    for col in categorical_features:
            data_new[col] = label_enc.fit_transform(data_new[col])

    print(data_new)

    data_new_f = pd.get_dummies(data_new, columns=dummy_features, drop_first=True)

    return data_new_f