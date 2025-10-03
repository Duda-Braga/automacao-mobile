import time
from appium import webdriver
from appium .options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:deviceName": "emulator-5554",
    "appium:automationName": "UiAutomator2",
    # start the aplication
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

# Selects the first item from the product list.

bolsa_cinza = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.ImageView[@content-desc=\"Product Image\"])[1]")
bolsa_cinza.click()

# Changes the color to Green.
time.sleep(1)
cor_verde = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Green color")
cor_verde.click()

# Increases the quantity to 2.
time.sleep(1)
aumentar_um_qntd = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Increase item quantity")
aumentar_um_qntd.click()

# Adds to cart.
time.sleep(1)
adiconar_carrinho = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Tap to add product to cart")
adiconar_carrinho.click()

# Opens the cart.
time.sleep(1)
botao_carrinho = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Displays number of items in your cart")
botao_carrinho.click()

# In the cart, decreases the quantity to 1.
time.sleep(1)
diminuir_um_qntd = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Decrease item quantity")
diminuir_um_qntd.click()

# Proceeds to checkout.
botao_checkout = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Confirms products for checkout")
botao_checkout.click()

# On the Login screen, enters "UserTest" and "PasswordTest" and logs in.
time.sleep(1)
campo_usuario = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/nameET")
campo_usuario.click()
campo_usuario.send_keys("UserTest")

campo_senha = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/passwordET")
campo_senha.click()
campo_senha.send_keys("PasswordTest")

botao_login = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/loginBtn")
botao_login.click()

# On the Checkout screen, fills in all values and proceeds.
time.sleep(1)
campo_nome = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/fullNameET")
campo_nome.click()
campo_nome.send_keys("Duda Linda")

campo_endereco_um = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/address1ET")
campo_endereco_um.click()
campo_endereco_um.send_keys("Casinha 123")

campo_endereco_dois = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/address2ET")
campo_endereco_dois.click()
campo_endereco_dois.send_keys("Casinha 345")

campo_cidade = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/cityET")
campo_cidade.click()
campo_cidade.send_keys("Cidadinha")

campo_estado = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/stateET")
campo_estado.click()
campo_estado.send_keys("Estadinho")

campo_zipcode = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/zipET")
campo_zipcode.click()
campo_zipcode.send_keys("89750")

campo_pais = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/countryET")
campo_pais.click()
campo_pais.send_keys("Brasil")

botao_pagamento = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/paymentBtn")
botao_pagamento.click()

# On the Payment screen, fills in all data and proceeds.
time.sleep
campo_nome_checkout = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/nameET")
campo_nome_checkout.click()
campo_nome_checkout.send_keys("Duda Linda")

campo_num_cartao = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/cardNumberET")
campo_num_cartao.click()
campo_num_cartao.send_keys("1234 5678 9101 1123")

campo_validade = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/expirationDateET")
campo_validade.click()
campo_validade.send_keys("0126")

campo_cvv = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/securityCodeET")
campo_cvv.click()
campo_cvv.send_keys("123")

botao_revisao_pedido = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/paymentBtn")
botao_revisao_pedido.click()

# On the Checkout screen, just proceeds.
time.sleep(1)
botao_place_order = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Completes the process of checkout")
botao_place_order.click()
# Enters the "Checkout Complete" screen.
time.sleep(1)
confirmacao_ckeckout = driver.find_elements(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/completeTV")
assert confirmacao_ckeckout != []

driver.quit()
