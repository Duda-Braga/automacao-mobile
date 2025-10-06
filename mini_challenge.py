import time
from appium import webdriver
from appium .options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:deviceName": "emulator-5554",
    "appium:automationName": "UiAutomator2",
    "appium:appPackage": "com.saucelabs.mydemoapp.android",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True,
    "appWaitActivity": "com.saucelabs.mydemoapp.android.view.activities.MainActivity",
    "appWaitDuration": 30000, # opcional, tempo de espera em ms (30s)
    "uiautomator2ServerLaunchTimeout": 30000,
    "uiautomator2ServerInstallTimeout": 30000
})


driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
time.sleep(1)

expected_orange_backpack_name = "Sauce Labs Backpack (orange)"
expected_my_cart_screen_text = "My Cart"
expected_unity_value_orange_backpack = "$ 29.99"
unity_product = 2
expected_login_screen_text = "Login"
expected_empty_user_error_mssg = "Username is required"
expected_empty_password_error_mssg = "Enter Password"
username = "user test"
expecteed_shipment_adress_screen_mssg = "Enter a shipping address"
expecteed_pay_method_screen_mssg = "Enter a payment method"
expected_review_order_screen_mssg = "Review your order"


#checkou info
full_name = "Test Person"
address_one = "little house 111"
address_two = "big house 222"
city = "Aracaju"
state = "Sergipe"
zip_code = "123456"
country = "Brasil"
card_number = "1234567809101112"
expiration_date = "03/30"
security_code = "456"

# Start the application and ensure that the home screen has loaded.
home_screen = driver.find_elements(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/productTV")
assert home_screen != [], "Home screen page did not load"

# Select the product Sauce Labs Backpack (orange) from the list of products 
orange_backpack = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.ImageView[@content-desc='Product Image'])[3]")
orange_backpack.click()

# validate if it opens
time.sleep(1)
orange_backpack_widget_name = driver.find_elements(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/productTV")
assert orange_backpack_widget_name != [], "Orange Backpack page did not open"
actual_orange_backpack_widget_name = orange_backpack_widget_name[0].text
assert expected_orange_backpack_name == actual_orange_backpack_widget_name, "Wrong backpack page opened"

# Decrease the quantity of products by pressing '-' and validate that the quantity has decreased by 1 unit
qntt_orange_backpack = int(driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/noTV").text)
less_button = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/minusIV")
less_button.click()
new_qntt_orange_backpack = int(driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/noTV").text)
assert qntt_orange_backpack - new_qntt_orange_backpack == 1, f"Quantity should be {qntt_orange_backpack - 1} but is {new_qntt_orange_backpack}"

# Also validate that when you reach zero quantity of products the Add to cart button will become inactive
if (new_qntt_orange_backpack == 0):
    add_cart_button = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/cartBt")
    assert add_cart_button.is_enabled() == False, "Add to cart button should not work"

# Increase the quantity of products by pressing '+' and check that the quantity has increased by 1 unit
qntt_orange_backpack = int(driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/noTV").text)
plus_button = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/plusIV")
plus_button.click()
new_qntt_orange_backpack = int(driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/noTV").text)
assert new_qntt_orange_backpack - qntt_orange_backpack == 1, f"Quantity should be {qntt_orange_backpack + 1} but is {new_qntt_orange_backpack}"

# Also check that when you reach more than zero units the Add to cart button will become active
if (new_qntt_orange_backpack != 0):
    assert add_cart_button.is_enabled(), "Add to cart button should  work"

# Add another unit by pressing +, make sure you have 2 units and click on the Add to cart button.
while(new_qntt_orange_backpack < 2):
    plus_button.click()
    new_qntt_orange_backpack = int(driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/noTV").text)
assert new_qntt_orange_backpack == 2, "It must have two items to be added"
add_cart_button.click()

# Validate that a circle has appeared in the cart icon informing you of the exact number of items you have added to the cart
qntt_cart_itens = driver.find_elements(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/cartTV")
assert qntt_cart_itens != [], "Cart circle does not exist"
num_qntt_cart_itens = int(qntt_cart_itens[0].text)
assert num_qntt_cart_itens == new_qntt_orange_backpack, "Quantity in cart differs from the amount added"

# Open the cart page by clicking on the cart icon
cart_icon = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/cartIV")
cart_icon.click()

# Validate that the My Cart screen has been opened
time.sleep(1)
my_cart_screen = driver.find_elements(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/productTV")
assert my_cart_screen != [], "Cart scren did not open"
actual_my_cart_screen_text = my_cart_screen[0].text
assert actual_my_cart_screen_text == expected_my_cart_screen_text, "Wrong page, expected to be in My Cart"

# Validate that your product is correct
my_cart_orange_backpack = driver.find_elements(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/titleTV")
assert my_cart_orange_backpack != [], "Product is not in the cart"
assert  my_cart_orange_backpack[0].text == expected_orange_backpack_name, "Wrong Product name in the cart"

# Validate that the unit value is as expected
actual_unity_value_orange_backpack = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/priceTV").text
assert actual_unity_value_orange_backpack == expected_unity_value_orange_backpack, "Wrong unity value of Orange Backapcack"

# Validate that the quantity is correct in the field below the product photo
actual_qtt_backpack_cart = int(driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/noTV").text)
assert actual_qtt_backpack_cart == new_qntt_orange_backpack, "The quantity of orange backpacks differs"

# Validate that the quantity is correct in the Total: x Items field
actual_total_qtt = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/itemsTV").text
assert int(actual_total_qtt[0]) == (unity_product), "Wrong total items in cart"

# Validate that the total value of the purchase is as expected for 2 units of the product
total_price_cart = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/totalPriceTV").text
actual_total_price_cart = float(total_price_cart[2:])
expected_total_price_cart = (actual_qtt_backpack_cart * float(expected_unity_value_orange_backpack[2:]))
assert actual_total_price_cart == expected_total_price_cart, "Wrong total value in cart for 2 products"

# Click on the Proceed To Checkout button
checkout_button = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/cartBt")
checkout_button.click()

# Validate that the Login screen has been displayed
time.sleep(1)
login_screen = driver.find_elements(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/loginTV")
assert login_screen != [], "Login screen did not load"
actual_login_screen_text = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/loginTV").text
assert actual_login_screen_text == expected_login_screen_text, "Wrong screen loaded, it should be login screen"

# Try to log in without entering Username and Password and validate the error in the Username field
login_button = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/loginBtn")
login_button.click()
time.sleep(1)
empty_user_error = driver.find_elements(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/nameErrorTV")
assert empty_user_error != [], "Error in the Username field for empty field did not appear"
actual_empty_user_error_mssg = empty_user_error[0].text
assert actual_empty_user_error_mssg == expected_empty_user_error_mssg, "Wrong message for login with empty username field"

# Try to log in without entering Password and validate the error in the Password field
username_field = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/nameET")
username_field.click()
username_field.send_keys(username)
login_button.click()
time.sleep(1)
empty_password_error = driver.find_elements(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/passwordErrorTV")
assert empty_password_error != [], "Error in the Password field for empty field did not appear"
actual_empty_password_error_mssg = empty_password_error[0].text
assert actual_empty_password_error_mssg == expected_empty_password_error_mssg, "Wrong message for login with empty password field"

# Capture the first Username from the Usernames list at the bottom of the screen and enter this value in the Username field
first_user_list = driver.find_element(by=AppiumBy.ID, value = "com.saucelabs.mydemoapp.android:id/username1TV")
first_user_list.click()

# Capture the Password from the Password list at the bottom of the screen and enter this value in the Password field
password_list = driver.find_element(by=AppiumBy.ID, value = "com.saucelabs.mydemoapp.android:id/password1TV")
password_list.click()

# Click on the Login button
login_button.click()

# Validate that the Checkout, Shipment Address screen has been displayed
time.sleep(1)
shipment_address_screen = driver.find_elements(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/enterShippingAddressTV")
assert shipment_address_screen != [], "Checkout, Shipment Address screen did not load"
actual_shipment_adress_screen_mssg = shipment_address_screen[0].text
assert actual_shipment_adress_screen_mssg == expecteed_shipment_adress_screen_mssg, "Wrong page loaded, it should be shipment address"

# Enter information in all the form fields and proceed to payment.
full_name_field = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/fullNameET")
full_name_field.send_keys(full_name)

address_one_field = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/address1ET")
address_one_field.send_keys(address_one)

address_two_field = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/address2ET")
address_two_field.send_keys(address_two)

city_field = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/cityET")
city_field.send_keys(city)

state_field = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/stateET")
state_field.send_keys(state)

zip_code_field = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/zipET")
zip_code_field.send_keys(zip_code)

country_field = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/countryET")
country_field.send_keys(country)

to_payment_btn = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/paymentBtn")
to_payment_btn.click()

# PLUS: Validate all the required fields and their errors when trying to submit the payment without entering these fields


# Validate that the Checkout, Payment screen has been displayed
time.sleep(1)
payment_method_screen = driver.find_elements(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/enterPaymentMethodTV")
assert payment_method_screen != [], "Checkout, Payment Method screen did not load"
actual_pay_method_screen_mssg = payment_method_screen[0].text
assert actual_pay_method_screen_mssg == expecteed_pay_method_screen_mssg, "Wrong page loaded, it should be payment method"

# Enter the values in the corresponding fields and keep the check-box selected
full_name_field = driver.find_element(by=AppiumBy.ID, value= "com.saucelabs.mydemoapp.android:id/nameET")
full_name_field.send_keys(full_name)

card_number_field = driver.find_element(by=AppiumBy.ID, value= "com.saucelabs.mydemoapp.android:id/cardNumberET")
card_number_field.send_keys(card_number)

expiration_date_field = driver.find_element(by=AppiumBy.ID, value= "com.saucelabs.mydemoapp.android:id/expirationDateET")
expiration_date_field.send_keys(expiration_date)

security_code_field = driver.find_element(by=AppiumBy.ID, value= "com.saucelabs.mydemoapp.android:id/securityCodeET")
security_code_field.send_keys(security_code)

payment_checkbox = driver.find_element(by=AppiumBy.ID, value= "com.saucelabs.mydemoapp.android:id/billingAddressCB")
if(payment_checkbox.get_attribute("checked") == False):
    payment_checkbox.click() #enable checkbox


# PLUS: Validate all mandatory fields.
# PLUS: Uncheck the Checkbox and Validate all required fields and their errors when trying to submit the payment without entering these fields.

# Proceed to the review by clicking on the Review Order button
review_order_btn = driver.find_element(by=AppiumBy.ID, value= "com.saucelabs.mydemoapp.android:id/paymentBtn")
review_order_btn.click()

# Validate that the Checkout, Review your order screen has been displayed.
time.sleep(1)
review_order_screen = driver.find_elements(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/enterShippingAddressTV")
assert review_order_screen != [], "Review your order screen did not load"
actual_review_order_screen_mssg = review_order_screen[0].text
assert actual_review_order_screen_mssg == expected_review_order_screen_mssg, "Wrong page loaded, it should be review your order"

# Validate the product's unit information such as Name and Value
review_product_name = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/titleTV").text
assert review_product_name == expected_orange_backpack_name, f"Wrong producto name, it should be {expected_orange_backpack_name}"

review_unity_value = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/priceTV").text
assert review_unity_value == expected_unity_value_orange_backpack, f"Wroong unity value, it should be {expected_unity_value_orange_backpack}"


# Validate that the Deliver Address and Payment Method information is correct
review_full_name = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/fullNameTV").text
assert review_full_name == full_name, "Wrong name in review order address screen"

review_address_one = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/addressTV").text
assert review_address_one == address_one, "Wrong address one in review order address screen"

review_city_state = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/cityTV").text
list_review_city_state = review_city_state.split(", ")
assert list_review_city_state[0] == city, "Wrong City in review order address screen"
assert list_review_city_state[1] == state, "Wrong State in review order address screen"

review_country_zip = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/countryTV").text
list_review_country_zip = review_country_zip.split(", ")
assert list_review_country_zip[0] == country, "Wrong Country in review order address screen"
assert list_review_country_zip[1] == zip_code, "Wrong Zip Code in review order address screen"

#scroll
size = driver.get_window_size()
screen_width = size['width']
screen_height = size['height']
driver.execute_script("mobile: scrollGesture", {
    "left": 0,
    "top": screen_height * 0.3,
    "width": screen_width,
    "height": screen_height * 0.5,
    "direction": "down",
    "percent": 1.0
})

review_pay_full_name = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/cardHolderTV").text
assert review_pay_full_name == full_name, "Wrong Name in payment review order screen"

review_card_number = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/cardNumberTV").text
assert review_card_number == card_number, "Wrong Card Number in payment review order screen"

review_expo_date = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/expirationDateTV").text
assert review_expo_date[5:] == expiration_date, "Wrong Expiration Date in payment review order screen"


# Validate that the total value of the items plus the Freight value is correct.

review_final_value = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/totalAmountTV").text
review_freight = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/amountTV").text
expected_final_value = actual_total_price_cart + float(review_freight[3:]) 
actual_final_value = float(review_freight[3:])
assert actual_final_value == expected_final_value, "Wrong sum of final price with freight"
print("PEGOUU \n \n \n \n")

# Click on the Place Order button
# Validate that the Checkout Complete screen has been displayed
# Click on the Continue Shopping button
# Validate that the Products screen has been displayed and that the cart is empty.


#driver.quit()
