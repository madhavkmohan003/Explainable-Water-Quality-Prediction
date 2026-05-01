from flask import Flask, render_template, request
import joblib
import google.generativeai as genai

app = Flask(__name__)

# 🔷 Load model
model = joblib.load("svm.pkl")

# 🔷 Configure Gemini (PUT YOUR KEY HERE)
genai.configure(api_key="AIzaSyCWUf4SHAvB2CzsvUM6XlLHMNrfoMBoLJU")


# 🔷 Clean 5–6 line output
def clean_text(text):
    lines = text.split("\n")
    clean_lines = [l.strip() for l in lines if l.strip()]
    return " ".join(clean_lines[:6])


# 🔷 Fallback (if Gemini fails)
def explain_water_quality(data, prediction):
    issues = []
    suggestions = []

    if data['ph'] < 6.5:
        issues.append("low pH (acidic water)")
        suggestions.append("use alkaline filter")
    elif data['ph'] > 8.5:
        issues.append("high pH (basic water)")
        suggestions.append("use neutralization")

    if data['turbidity'] > 5:
        issues.append("high turbidity")
        suggestions.append("apply filtration")

    if data['solids'] > 500:
        issues.append("high dissolved solids")
        suggestions.append("use reverse osmosis")

    if prediction == 1:
        return "Water is safe. All parameters are within acceptable limits and suitable for drinking."

    if issues:
        return (
            "Water is unsafe due to " + ", ".join(issues) +
            ". These conditions may affect safety and quality. " +
            "Suggested actions include " + ", ".join(suggestions) +
            ". Regular monitoring is recommended."
        )

    return "Water is unsafe due to chemical imbalance. Proper treatment and testing are recommended."


# 🔷 Gemini Explanation
def explain_with_gemini(data, prediction):
    try:
        print("Gemini API called")

        prompt = f"""
        You are a water quality expert.

        Water parameters:
        pH: {data['ph']}
        Hardness: {data['hardness']}
        Solids: {data['solids']}
        Chloramines: {data['chloramines']}
        Sulfate: {data['sulfate']}
        Conductivity: {data['conductivity']}
        Organic Carbon: {data['organicCarbon']}
        Trihalomethanes: {data['trihalomethanes']}
        Turbidity: {data['turbidity']}

        Prediction: {"Safe" if prediction == 1 else "Unsafe"}

        Give explanation in 5–6 lines:
        - mention key issues
        - explain impact
        - suggest improvements
        Keep it simple and clear.
        """

        model_ai = genai.GenerativeModel("gemini-2.5-flash")
        response = model_ai.generate_content(prompt)

        cleaned = clean_text(response.text)

        return cleaned

    except Exception as e:
        print("Gemini error:", e)
        return "AI explanation unavailable"


# 🔷 Routes
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict_waterQ', methods=['POST'])
def predict_waterQ():

    data = {
        "ph": float(request.form["ph"]),
        "hardness": float(request.form["hardness"]),
        "solids": float(request.form["solids"]),
        "chloramines": float(request.form["chloramines"]),
        "sulfate": float(request.form["sulfate"]),
        "conductivity": float(request.form["conductivity"]),
        "organicCarbon": float(request.form["organicCarbon"]),
        "trihalomethanes": float(request.form["trihalomethanes"]),
        "turbidity": float(request.form["turbidity"])
    }

    input_values = list(data.values())
    prediction = model.predict([input_values])[0]

    prediction_text = "Safe" if prediction == 1 else "Unsafe"

    # 🔥 Gemini + fallback
    explanation = explain_with_gemini(data, prediction)

    if "unavailable" in explanation or explanation.strip() == "":
        explanation = explain_water_quality(data, prediction)

    return render_template(
        'result.html',
        prediction=prediction_text,
        explanation=explanation
    )


if __name__ == '__main__':
    app.run(debug=True)