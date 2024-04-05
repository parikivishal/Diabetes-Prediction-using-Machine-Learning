from django.shortcuts import render
import pickle
import numpy as np

# Create your views here.
def home(request):
    return render(request,"index.html")
def predict(request):
    if request.method == "POST":
        age = request.POST.get('age')
        if age == "40-49":
            age1 = 0
        elif age == "50-59":
            age1 = 1
        elif age == "60 or older":
            age1 = 2
        else:
            age1 = 3
        gender = request.POST.get('gender')
        request.session['genders']=gender
        if gender == "Female":
            gender1 = 0
        else:
            gender1 = 1
        fdiabetes = request.POST.get('fdiabetes')
        if fdiabetes == "No":
            fdiabetes1 = 0
        else:
            fdiabetes1 = 1
        highbp = request.POST.get('highbp')
        if highbp == "No":
            highbp1 = 0
        else:
            highbp1 = 1
        pactive = request.POST.get('pactive')
        if pactive == "less than half an hr":
            pactive1 = 0
        elif pactive == "more than half an hr":
            pactive1 = 1
        elif pactive == "none":
            pactive1 = 2
        else:
            pactive1 = 3
        bmi = request.POST.get('bmi')
        smoking = request.POST.get('smoking')
        if smoking == "No":
            smoking1= 0
        else:
            smoking1 = 1
        sleep = request.POST.get('sleep')
        ssleep = request.POST.get('ssleep')
        alcohol = request.POST.get('alcohol')
        if alcohol == "No":
            alcohol1 = 0
        else:
            alcohol1 = 1
        medicine = request.POST.get('medicine')
        if medicine == "No":
            medicine1 = 0
        elif medicine == "Regular":
            medicine1 = 2
        else:
            medicine1 = 1
        junk = request.POST.get('junk')
        if junk == "Always":
            junk1 = 0
        elif junk == "Ocasionally":
            junk1 = 1
        elif junk == "Often":
            junk1 = 2
        else:
            junk1 = 3
        stress = request.POST.get('stress')
        if stress == "Always":
            stress1 = 0
        elif stress == "Not at all":
            stress1 = 1
        elif stress == "Sometimes":
            stress1 = 2
        else:
            stress1 =3
        bplevel = request.POST.get('bplevel')
        if bplevel == "Low":
            bplevel1 = 1
        elif bplevel == "Normal":
            bplevel1 = 2
        else:
            bplevel1 = 0
        pregnancies = request.POST.get('pregnancies')
        pdiabetes = request.POST.get('pdiabetes')
        if pdiabetes == "No":
            pdiabetes1 = 0
        else:
            pdiabetes1 = 1
        ufrequency = request.POST.get('ufrequency')
        if ufrequency == "Not Much":
            ufrequency1 = 0
        else:
            ufrequency1 = 1
        model = pickle.load(open("model/model.pkl", "rb"))
        inp = np.array([age1, gender1, fdiabetes1, highbp1, pactive1, bmi, smoking1, alcohol1, sleep, ssleep, medicine1, junk1,
                        stress1, bplevel1, pregnancies, pdiabetes1, ufrequency1])
        arr = inp.reshape(1, -1)
        ans = model.predict(arr)
        res= round(float(ans))
        print(res)
        if res == 1:
            result = "You have Diabetes"
            tip = "Don't Panic!! We have a diet plan for you to control your diabetes! "
        else:
            result = "No Diabetes"
            tip = "Cool!! you don't have diabetes bit we have a diet plan to avoid in further days."
        request.session['result'] = result
        return render(request, "result.html", {"inp1":age, "inp2": gender, "inp3": fdiabetes, "inp4": highbp,
                                                "inp5": pactive, "inp6": bmi, "inp7": smoking, "inp8":sleep, "inp9":ssleep,
                                                "inp10": alcohol, "inp11": medicine, "inp12": junk, "inp13": stress,
                                                "inp14": bplevel, "inp15": pregnancies, "inp16":pdiabetes,
                                                "inp17": ufrequency, "result2": result, "tips": tip})
    return render(request,"predict.html")
def dietprediction(request):
    if request.method == "POST":
        height = int(request.POST.get('height'))
        weight = int(request.POST.get('weight'))
        age = int(request.POST.get('age'))
        activity = request.POST.get('activity')
        gender = request.session.get('genders')
        dres = request.session.get('result')
        if gender == "Female":
            bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
            if activity == "little":
                calorie = bmr * 1.2
            elif activity == "light":
                calorie = bmr * 1.375
            elif activity == "moderate" or activity == "hard":
                calorie = bmr * 1.725
            else:
                calorie = bmr * 1.9
        else:
            bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
            if activity == "little":
                calorie = bmr * 1.2
            elif activity == "light":
                calorie = bmr * 1.375
            elif activity == "moderate" or activity == "hard":
                calorie = bmr * 1.725
            else:
                calorie = bmr * 1.9

        return render(request,'finalresult.html',{"in1":dres, "in2":calorie})
    return render(request,'dietprediction.html')

