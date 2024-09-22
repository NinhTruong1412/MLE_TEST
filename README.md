# Machine Learning Engineer Home Test

## 1. Overview
This repo is for experimenting a ML model for monthly sale prediction and buiding a tool for intenal users

* Task 1: Modeling : Forecast the total amount of products sold in every shop for the test set with provided with historical sales data on daily basis
* Taks 2: Deploy this model to internal users

## 🚨 WARNING: This model is facing with over fitting problems, need to enhance more, I don't have much time to spend on optimizing so i skip the experiment phase for now and continue implementing deployment phase.

---

## 2. Works

### 2.1. Modeling data
#### a. Data overview

Files:
- train.csv - the training set. Reference time from 2013-01 to 2015-10.
- test.csv - the test set. Reference time 2015-11.
- items.csv - list of all items/products.
- item_categories.csv  - list of all categories.
- shops.csv- list of all shops.

Fields:
- ID - an Id that represents a (Shop, Item) tuple within the test set
- shop_id - unique identifier of a shop
- item_id - unique identifier of a product
- item_category_id - unique identifier of item category
- item_cnt_day - number of products sold. You are predicting a monthly amount of this measure
- item_price - current price of an item
- date - date in format dd/mm/yyyy
- date_block_num - a consecutive month number, used for convenience. 2013-01 is 0, 2013-02 is 1,..., 2015-10 is 33
- item_name - name of item
- shop_name - name of shop
- item_category_name - name of item category

#### b. Experiment

+ Exploring data (Loading, cleaning, EDA)
+ Feature enngineering
+ Modeling data
+ Evaluation
**Note**: [View on Notebook](https://github.com/NinhTruong1412/MLE_TEST/tree/main/src/app)

### 2.2. Deploying sale prediction model
I built a API for internal users, it can be integrated easily to many other tools and platform.

#### a. How to deploy ?
+ Install requirement
+ Test API local cmd: `make run-app`
+ Deploy and test API with docker: `make test-serving-image IMAGE_NAME={image-name} IMAGE_VERSION={version-name}`

#### b. API instruction
+ Endpoint: `/api/v1/predict/{shop_id}/{item_id}`
+ Method: `POST`
+ Params: 
    ```
    {
        "shop_id": 36,
        "item_id": 1
    }
    ```
+ Response: 
    ```
    {
        "shop_id": 36,
        "item_id": 1,
        "total_month_sale": 0.5
    }
    ```

