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

# Validate that the quantity is correct in the field below the product photo
# Validate that the quantity is correct in the Total: x Items field
# Validate that the total value of the purchase is as expected for 2 units of the product
# Click on the Proceed To Checkout button
# Validate that the Login screen has been displayed
# Try to log in without entering Username and Password and validate the error in the Username field
# Try to log in without entering Password and validate the error in the Password field
# Capture the first Username from the Usernames list at the bottom of the screen and enter this value in the Username field
# Capture the Password from the Password list at the bottom of the screen and enter this value in the Password field
# Click on the Login button
# Validate that the Checkout, Shipment Address screen has been displayed
# Enter information in all the form fields and proceed to payment.
# PLUS: Validate all the required fields and their errors when trying to submit the payment without entering these fields
# Validate that the Checkout, Payment screen has been displayed
# Enter the values in the corresponding fields and keep the check-box selected
# PLUS: Validate all mandatory fields.
# PLUS: Validate all required fields and their errors when trying to submit the payment without entering these fields.
# Validate that the Checkout, Payment screen has been displayed
# Enter the values in the corresponding fields and keep the check-box selected
# PLUS: Validate all required fields and their errors when trying to submit the payment without entering these fields.
# PLUS: Checkbox
# Proceed to the review by clicking on the Review Order button
# Validate that the Checkout, Review your order screen has been displayed.
# Validate that the Deliver Address and Payment Method information is correct
# Validate the product's unit information such as Name and Value
# Validate that the total value of the items plus the Freight value is correct.
# Click on the Place Order button
# Validate that the Checkout Complete screen has been displayed
# Click on the Continue Shopping button
# Validate that the Products screen has been displayed and that the cart is empty.

#driver.quit()
