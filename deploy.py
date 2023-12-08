import random 


from flask import Flask

from flask import Flask, render_template, redirect, url_for, request
price1 = random.uniform(1000,100000) 
app= Flask(__name__)
@app.route('/')
def home():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Styled Form with 4 Elements</title>
    <style>
    
        body {
            font-family: 'Arial', sans-serif;
             background-image: url('https://th.bing.com/th/id/OIP.iiB5yG3NLqKr1C93yVMtoAHaE8?rs=1&pid=ImgDetMainhttps://th.bing.com/th/id/OIP.iiB5yG3NLqKr1C93yVMtoAHaE8?rs=1&pid=ImgDetMain'); /* Replace 'your-background-image.jpg' with the actual path to your image */
            background-size: cover;
            background-position: center;
            background-color: #f4f4f4;
            margin: 20px;
        }

        h2 {
            color: #333;
        }

        form {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            margin: auto;
        }

        label {
            display: block;
            margin-bottom: 8px;
            color: #333;
        }

        input,
        textarea,
        select {
            width: 100%;
            padding: 8px;
            margin-bottom: 16px;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        select {
            height: 34px;
        }

        input[type="submit"] {
            background-color: #4caf50;
            color: #fff;
            cursor: pointer;
        }

        input[type="submit"]:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>


<form action="/submit" method="post">

    <label for="input1">Quantity:</label>
    <input type="number" id="input1" name="Quantity" pattern="\d+" title="Please enter a valid integer" required>

    <label for="input2">Discount:</label>
    <input type="number" id="input2" name="Discount" required>

    <label for="input3">Profit:</label>
    <input type="number" id="input3" name="Profit" required>

    <label for="input4">Shipping Cost:</label>
    <input type="number" id="input4" name="Shipping_Cost" pattern="\d+" title="Please enter a valid integer" required>

    <label for="selectCategory">Category:</label>
    <select id="selectCategory" name="Category" required>
        <option value="Office_Supplies">Office Supplies</option>
        <option value="Technology">Technology</option>
    </select>

    <label for="selectSegment">Segment:</label>
    <select id="selectSegment" name="Segment" required>
        <option value="Home_Office">Home Office</option>
        <option value="Corporate">Corporate</option>
    </select>

    <label for="selectSubCategory">Sub Category:</label>
    <select id="selectSubCategory" name="Sub_Category" required>
        <option value="Binders">Binders</option>
        <option value="Storage">Storage</option>
        <option value="Accessories">Accessories</option>
        <option value="Supplies">Supplies</option>
        <option value="Bookcases">Bookcases</option>
    </select>

    <input type="submit" value="Submit">
</form>

</body>
</html>
'''
# Handle the form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get form data from the request
    quantity = request.form.get('Quantity')
    discount = request.form.get('Discount')
    profit = request.form.get('Profit')
    shipping_cost = request.form.get('Shipping_cost')
    category = request.form.get('Category')
    Segment= request.form.get('Segment')
    Sub_Category =request.form.get('Sub Category')
       #data = {
    #   'Quantity': [Quantity],
    #    'Discount': [Discount],
    #    'Profit': [Profit],
    #    'Shipping Cost': [Shipping_Cost],
    #    'category'=[category],
    #    'segment'=[segment],
    #    'Sub_Category' =[Sub_Category]
    #          }
    # df = pd.DataFrame(data)


    #categorical_columns = ['Segment', 'Category', 'Sub-Category', 'Order Priority']
    #df5 = pd.get_dummies(df, columns=categorical_columns, drop_first=True)
    #df5.columns
    #model.load('my_keras_model')
    #price=model.predict(df)


    # Perform any necessary processing with form data here
    # For example, you might want to save the data to a database or perform calculations

    # Redirect to another HTML page (e.g., success.html)
    return redirect(url_for('success') )
# Display a success page
@app.route('/success')
def success():
    return render_template('a.html')
if __name__ == '__main__':
     app.run(debug=True)

