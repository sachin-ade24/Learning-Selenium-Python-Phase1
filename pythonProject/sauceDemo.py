import time
# from typing import List

from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = 'https://www.saucedemo.com/v1/index.html'
cssSelectorForUserName = '[placeholder="Username"]'
userNameText = 'standard_user'
passwordIdValue = 'password'
passwordText = 'secret_sauce'
xpathForLoginBtn = "//input[@id='login-button']"
actions = ActionChains(driver)

driver.maximize_window()
time.sleep(2)
driver.get(url)
time.sleep(0.5)
print("The Current url: ", driver.current_url)
time.sleep(2)
if driver.current_url == url:
    print("Test Case 1: Passed")
else:
    print("Test Case 1: Failed")
time.sleep(5)
print("The title of web page: " + driver.title)
time.sleep(1)
if driver.title == 'Swag Labs':
    print("Test Case 2: Passed")
else:
    print("Test Case 2: Failed")
time.sleep(1)
userName = driver.find_element(By.CSS_SELECTOR, cssSelectorForUserName)
time.sleep(1)
if userName.is_displayed():
    print("Test Case 3: Passed")
else:
    print("Test Case 3: Failed")
time.sleep(1)
if userName.tag_name == 'input':
    print("Test Case 4: Passed")
else:
    print("Test Case 4: Failed")
time.sleep(1)
if userName.get_attribute('name') == 'user-name':
    print("Test Case 5: Passed")
else:
    print("Test Case 5: Failed")
time.sleep(1)
if userName.value_of_css_property('font-size') == '18px':
    print("Test Case 6: Passed")
else:
    print("Test Case 6: Failed")
time.sleep(1)
if userName.value_of_css_property('border-bottom-color') == 'rgba(204, 204, 204, 1)':
    print("Test Case 7: Passed")
else:
    print("Test Case 7: Failed")
time.sleep(1)
if userName.value_of_css_property('color') == 'rgba(0, 0, 0, 1)':
    print("Test Case 8: Passed")
else:
    print("Test Case 8: Failed")
time.sleep(1)
if userName.value_of_css_property('background-color') == 'rgba(255, 255, 255, 1)':
    print("Test Case 9: Passed")
else:
    print("Test Case 9: Failed")
time.sleep(1)
userName.send_keys(userNameText)
time.sleep(2)
pwd = driver.find_element(By.ID, passwordIdValue)
if pwd.is_enabled():
    print("Test Case 10: Passed")
else:
    print("Test Case 10: Failed")
time.sleep(1)
if pwd.get_attribute('id') == 'password':
    print("Test Case 11: Passed")
else:
    print("Test Case 11: Failed")
time.sleep(1)
if pwd.value_of_css_property('background-color') == 'rgba(255, 255, 255, 1)':
    print("Test Case 12: Passed")
else:
    print("Test Case 12: Failed")
time.sleep(1)
pwd.send_keys(passwordText)
time.sleep(2)
loginBtn = driver.find_element(By.XPATH, xpathForLoginBtn)
if loginBtn.get_attribute('class') == 'btn_action':
    print("Test Case 13: Passed")
else:
    print("Test Case 13: Failed")
time.sleep(1)
if loginBtn.value_of_css_property('background-color') == 'rgba(226, 35, 26, 1)':
    print("Test Case 14: Passed")
else:
    print("Test Case 14: Failed")
time.sleep(1)
if loginBtn.value_of_css_property('color') == 'rgba(255, 255, 255, 1)':
    print("Test Case 15: Passed")
else:
    print("Test Case 15: Failed")
time.sleep(1)
loginBtn.click()
time.sleep(4)

sauceLabsBikeLight = driver.find_element(By.XPATH, "(//div[@class='inventory_item_desc'])[2]").text
print(sauceLabsBikeLight)

# Products
productsUrl = "https://www.saucedemo.com/v1/inventory.html"
productsCurrentUrl = driver.current_url
print("Url for the Products page:", productsCurrentUrl)
time.sleep(1)
products = driver.find_element(By.CSS_SELECTOR, '.product_label')
productsText = products.text
print("Products page heading:", productsText)
time.sleep(1)

# (//*[@class='product_sort_container'])/option[1]
# //div[contains(text(),'Sauce Labs Backpack')]/parent : : div
ddSelector = driver.find_element(By.CSS_SELECTOR, '.product_sort_container')
indexes = [0, 1, 2, 3, 0]
for index in indexes:
    Select(ddSelector).select_by_index(index)
    time.sleep(2)

selectorForNoOfOptionsInTheDd = driver.find_elements(By.CSS_SELECTOR, 'option')
noOfOptionsInTheDd = len(selectorForNoOfOptionsInTheDd)
expectedNoOfOptionsInTheDd = 4
if noOfOptionsInTheDd == expectedNoOfOptionsInTheDd:
    print("Number of options in the dropdown:", noOfOptionsInTheDd)
else:
    print("Test Case Failed")
time.sleep(1)

ddOption1Text = driver.find_element(By.CSS_SELECTOR, 'option:nth-child(1)').text
print("Option0 text: ", ddOption1Text)
if ddOption1Text == 'Name (A to Z)':
    print('Test Case 16: Passed')
else:
    print('Test Case 16: Failed')
time.sleep(1)
ddOption2Text = driver.find_element(By.CSS_SELECTOR, 'option:nth-child(2)').text
print("Option1 text: ", ddOption2Text)
if ddOption2Text == "Name (Z to A)":
    print('Test Case 17: Passed')
else:
    print('Test Case 17: Failed')
time.sleep(1)
ddOption3Text = driver.find_element(By.CSS_SELECTOR, 'option:nth-child(3)').text
ddOption4Text = driver.find_element(By.CSS_SELECTOR, 'option:nth-child(4)').text

# ddOptions = ["Name (A to Z)", "Name (Z to A)", "Price (low to high)", "Price (high to low)"]
ddOptions = [ddOption1Text, ddOption2Text, ddOption3Text, ddOption4Text]
for index, ddOption in enumerate(ddOptions):
    Select(ddSelector).select_by_visible_text(ddOption)
    time.sleep(1)
    assert ddOption in ddOptions
    time.sleep(1)
    print("Dropdown option is:", index+1, ddOption)
sauceLabBackpack = driver.find_element(By.XPATH, "(//button[text()='ADD TO CART'])[1]")
time.sleep(1)
actualAddToCartText = sauceLabBackpack.text
print('Actual add to cart text: ', actualAddToCartText)
time.sleep(1)
expectedAddToCartText = 'ADD TO CART'
print('Expected add to cart text: ', expectedAddToCartText)
time.sleep(1)
assert 'ADD TO CART' in actualAddToCartText
print(actualAddToCartText, ' is right')
if actualAddToCartText == expectedAddToCartText:
    print('Test Case 18: Passed')
else:
    print('Test Case 18: Failed')
addAllItemsToCart = driver.find_elements(By.CSS_SELECTOR, 'button.btn_primary.btn_inventory')
lengthOfList = len(addAllItemsToCart)
print("length of list is", lengthOfList)
time.sleep(1)
for addToCartButton in addAllItemsToCart:
    actions.move_to_element(addToCartButton).click().perform()
    time.sleep(1)
actualNoOfItemsInTheCart = driver.find_element(By.CSS_SELECTOR, "[class*='shopping_cart_badge']")
print("Actual no. of items in the cart:", actualNoOfItemsInTheCart.text)
expectedNoOfItemsInTheCart = '6'
print("Expected no. of items in the cart: ", expectedNoOfItemsInTheCart)
time.sleep(1)
assert '6' in actualNoOfItemsInTheCart.text
print('Count is: 6')
if expectedNoOfItemsInTheCart == actualNoOfItemsInTheCart.text:
    print("Test case 19: Passed")
else:
    print("Test case 19: Failed")
time.sleep(1)
shoppingKart = driver.find_element(By.CSS_SELECTOR, "[class*='fa-shopping-cart']")
actions.move_to_element(shoppingKart).click(shoppingKart).perform()
time.sleep(2)

cartListSelectorForBackpack = driver.find_element(By.CSS_SELECTOR, ".cart_list .cart_item:nth-child(3)")
# * 1 *
# * 1 * Quantity
sauceLabsBackpackQuantity = cartListSelectorForBackpack.find_element(By.CSS_SELECTOR, ".cart_quantity")
sauceLabsBackpackQuantityText = sauceLabsBackpackQuantity.text
# * 1 * Item Name
backpackItemName = cartListSelectorForBackpack.find_element(By.CSS_SELECTOR, ".inventory_item_name")
backpackItemNameText = backpackItemName.text
print("\n(1)Item Name", backpackItemNameText, ":")
# * 1 * Item Description
backpackItemDescription = cartListSelectorForBackpack.find_element(By.CSS_SELECTOR, ".inventory_item_desc")
backpackItemDescriptionText = backpackItemDescription.text
# * 1 * Item Price
backpackItemPrice = cartListSelectorForBackpack.find_element(By.CSS_SELECTOR, ".inventory_item_price")
backpackItemPriceText = backpackItemPrice.text
# * 1 * Assertion
backPackItems = [["Quantity:", sauceLabsBackpackQuantityText], ["Item Name:", backpackItemNameText], ["Item description:", backpackItemDescriptionText], ["Item price:", backpackItemPriceText]]
for index, backPackItem in enumerate(backPackItems):
    assert backPackItem in backPackItems
    print(index+1, backPackItem)
    time.sleep(0.5)

cartListSelectorForBikeLight = driver.find_element(By.CSS_SELECTOR, ".cart_list .cart_item:nth-child(4)")
# * 2 *
# * 2 * Quantity sauceLabsBikeLight bikeLight
bikeLightQuantity = cartListSelectorForBikeLight.find_element(By.CSS_SELECTOR, ".cart_quantity")
bikeLightQuantityText = bikeLightQuantity.text
# * 2 * Item Name
bikeLightItemName = cartListSelectorForBikeLight.find_element(By.CSS_SELECTOR, ".inventory_item_name")
bikeLightItemNameText = bikeLightItemName.text
print("\n(2)Item Name", bikeLightItemNameText, ":")
# * 2 * Item Description
bikeLightItemDescription = cartListSelectorForBikeLight.find_element(By.CSS_SELECTOR, ".inventory_item_desc")
bikeLightItemDescriptionText = bikeLightItemDescription.text
# * 2 * Item Price
bikeLightItemPrice = cartListSelectorForBikeLight.find_element(By.CSS_SELECTOR, ".inventory_item_price")
bikeLightItemPriceText = bikeLightItemPrice.text
# * 2 * Assertion
bikeLightItems = [["Quantity:", bikeLightQuantityText], ["Item Name:", bikeLightItemNameText], ["Item description:", bikeLightItemDescriptionText], ["Item price:", bikeLightItemPriceText]]
for index, bikeLightItem in enumerate(bikeLightItems):
    assert bikeLightItem in bikeLightItems
    print(index+1, bikeLightItem)
    time.sleep(0.5)

cartListSelectorForBoltTShirt = driver.find_element(By.CSS_SELECTOR, ".cart_list .cart_item:nth-child(5)")
# * 3 *
# * 3 * Quantity sauceLabsBikeLight bikeLight
boltTShirtQuantity = cartListSelectorForBoltTShirt.find_element(By.CSS_SELECTOR, ".cart_quantity")
boltTShirtQuantityText = bikeLightQuantity.text
# * 3 * Item Name
boltTShirtItemName = cartListSelectorForBoltTShirt.find_element(By.CSS_SELECTOR, ".inventory_item_name")
boltTShirtItemNameText = boltTShirtItemName.text
print("\n(3)Item Name", boltTShirtItemNameText, ":")
# * 3 * Item Description
boltTShirtItemDescription = cartListSelectorForBoltTShirt.find_element(By.CSS_SELECTOR, ".inventory_item_desc")
boltTShirtItemDescriptionText = boltTShirtItemDescription.text
# * 3 * Item Price
boltTShirtItemPrice = cartListSelectorForBoltTShirt.find_element(By.CSS_SELECTOR, ".inventory_item_price")
boltTShirtItemPriceText = boltTShirtItemPrice.text
# * 3 * Assertion
boltTShirtItems = [["Quantity:", boltTShirtQuantityText], ["Item Name:", boltTShirtItemNameText], ["Item description:", boltTShirtItemDescriptionText], ["Item price:", boltTShirtItemPriceText]]
for index, boltTShirtItem in enumerate(boltTShirtItems):
    assert boltTShirtItem in boltTShirtItems
    print(index+1, boltTShirtItem)
    time.sleep(0.5)

cartListSelectorForLabsOnesie = driver.find_element(By.CSS_SELECTOR, ".cart_list .cart_item:nth-child(6)")
# * 4 *
# * 4 * Quantity sauceLabsBikeLight bikeLight
labsOnesieQuantity = cartListSelectorForLabsOnesie.find_element(By.CSS_SELECTOR, ".cart_quantity")
labsOnesieQuantityText = labsOnesieQuantity.text
# * 4 * Item Name
labsOnesieItemName = cartListSelectorForLabsOnesie.find_element(By.CSS_SELECTOR, ".inventory_item_name")
labsOnesieItemNameText = labsOnesieItemName.text
print("\n(4)Item Name", labsOnesieItemNameText, ":")
# * 4 * Item Description
labsOnesieItemDescription = cartListSelectorForLabsOnesie.find_element(By.CSS_SELECTOR, ".inventory_item_desc")
labsOnesieItemDescriptionText = labsOnesieItemDescription.text
# * 4 * Item Price
labsOnesieItemPrice = cartListSelectorForLabsOnesie.find_element(By.CSS_SELECTOR, ".inventory_item_price")
labsOnesieItemPriceText = labsOnesieItemPrice.text
# * 4 * Assertion
labsOnesieItems = [["Quantity:", labsOnesieQuantityText], ["Item Name:", labsOnesieItemNameText], ["Item description:", labsOnesieItemDescriptionText], ["Item price:", labsOnesieItemPriceText]]
for index, labsOnesieItem in enumerate(labsOnesieItems):
    assert labsOnesieItem in labsOnesieItems
    print(index + 1, labsOnesieItem)
    time.sleep(0.5)

cartListSelectorForFleeceJacket = driver.find_element(By.CSS_SELECTOR, ".cart_list .cart_item:nth-child(7)")
# * 5 *
# * 5 * Quantity sauceLabsBikeLight bikeLight
fleeceJacketQuantity = cartListSelectorForFleeceJacket.find_element(By.CSS_SELECTOR, ".cart_quantity")
fleeceJacketQuantityText = fleeceJacketQuantity.text
# * 5 *
# Item Name
fleeceJacketItemName = cartListSelectorForFleeceJacket.find_element(By.CSS_SELECTOR, ".inventory_item_name")
fleeceJacketItemNameText = fleeceJacketItemName.text
print("\n(5)Item Name", fleeceJacketItemNameText, ":")
# * 5 * Item Description
fleeceJacketItemDescription = cartListSelectorForFleeceJacket.find_element(By.CSS_SELECTOR, ".inventory_item_desc")
fleeceJacketItemDescriptionText = fleeceJacketItemDescription.text
# * 5 * Item Price
fleeceJacketItemPrice = cartListSelectorForFleeceJacket.find_element(By.CSS_SELECTOR, ".inventory_item_price")
fleeceJacketItemPriceText = fleeceJacketItemPrice.text
# * 5 * Assertion
fleeceJacketItems = [["Quantity:", fleeceJacketQuantityText], ["Item Name:", fleeceJacketItemNameText], ["Item description:", fleeceJacketItemDescriptionText], ["Item price:", fleeceJacketItemPriceText]]
for index, fleeceJacketItem in enumerate(fleeceJacketItems):
    assert fleeceJacketItem in fleeceJacketItems
    print(index + 1, fleeceJacketItem)
    time.sleep(0.5)

cartListSelectorForAllTheThingsTShirt = driver.find_element(By.CSS_SELECTOR, ".cart_list .cart_item:nth-child(8)")
# * 6 *
# * 6 * Quantity sauceLabsBikeLight bikeLight
allTheThingsTShirtQuantity = cartListSelectorForAllTheThingsTShirt.find_element(By.CSS_SELECTOR, ".cart_quantity")
allTheThingsTShirtQuantityText = allTheThingsTShirtQuantity.text
# * 6 *
# Item Name
allTheThingsTShirtItemName = cartListSelectorForAllTheThingsTShirt.find_element(By.CSS_SELECTOR, ".inventory_item_name")
allTheThingsTShirtItemNameText = allTheThingsTShirtItemName.text
print("\n(6)Item Name", allTheThingsTShirtItemNameText, ":")
# * 6 * Item Description
allTheThingsTShirtItemDescription = cartListSelectorForAllTheThingsTShirt.find_element(By.CSS_SELECTOR, ".inventory_item_desc")
allTheThingsTShirtItemDescriptionText = allTheThingsTShirtItemDescription.text
# * 6 * Item Price
allTheThingsTShirtItemPrice = cartListSelectorForAllTheThingsTShirt.find_element(By.CSS_SELECTOR, ".inventory_item_price")
allTheThingsTShirtItemPriceText = allTheThingsTShirtItemPrice.text
# * 6 * Assertion
allTheThingsTShirtItems = [["Quantity:", allTheThingsTShirtQuantityText], ["Item Name:", allTheThingsTShirtItemNameText], ["Item description:", allTheThingsTShirtItemDescriptionText], ["Item price:", allTheThingsTShirtItemPriceText]]
for index, allTheThingsTShirtItem in enumerate(allTheThingsTShirtItems):
    assert allTheThingsTShirtItem in allTheThingsTShirtItems
    print(index + 1, allTheThingsTShirtItem)
    time.sleep(0.5)

itemsList = [backPackItems, bikeLightItems, boltTShirtItems, labsOnesieItems, fleeceJacketItems, allTheThingsTShirtItems]
for itemInTheList in itemsList:
    assert itemInTheList in itemsList
    print("\nItems are as follows:\n", itemsList)

# checkout_button
checkoutBtn = driver.find_element(By.CSS_SELECTOR, "[class*='checkout_button']")
checkout = checkoutBtn.text
assert 'CHECKOUT' in checkout
print('\nCheckout button text:', checkout)
time.sleep(1)
backgroundColorOfCheckoutBtn = checkoutBtn.value_of_css_property('background-color')
expectedBackgroundColorOfCheckoutBtn = 'rgba(226, 35, 26, 1)'
assert expectedBackgroundColorOfCheckoutBtn in backgroundColorOfCheckoutBtn
print("Checkout button background color is:", backgroundColorOfCheckoutBtn)
colorOfCheckoutBtn = checkoutBtn.value_of_css_property('color')
expectedColorOfCheckoutBtn = 'rgba(255, 255, 255, 1)'
assert expectedColorOfCheckoutBtn in colorOfCheckoutBtn
print("Checkout button color is:", colorOfCheckoutBtn)
time.sleep(1)
checkoutBtn.click()
time.sleep(1)
noOfInputTagsInCheckoutInfo = driver.find_element(By.CSS_SELECTOR, ".checkout_info")\
    .find_elements(By.CSS_SELECTOR, "input")
noOfInputs = len(noOfInputTagsInCheckoutInfo)
expectedNoOInputTags = 3
if noOfInputs == expectedNoOInputTags:
    print("No. of input tags:", noOfInputs)
else:
    print("Test case failed")
time.sleep(1)
input_ = driver.find_element(By.CSS_SELECTOR, 'input')
firstName = driver.find_element(By.CSS_SELECTOR, '#first-name')
firstName.send_keys("Sachin")
time.sleep(1)
lastName = driver.find_element(By.CSS_SELECTOR, '#last-name')
lastName.send_keys("Ade")
time.sleep(1)
postalCode = driver.find_element(By.CSS_SELECTOR, '#postal-code')
postalCode.send_keys("431131")
time.sleep(1)
# #efefef div.checkout_buttons > input.btn_primary.cart_button
footer = driver.find_element(By.CSS_SELECTOR, 'div.checkout_buttons')
cancelBtnTag = footer.find_elements(By.CSS_SELECTOR, "a")
noOfCancelBtnTags = len(cancelBtnTag)
print("No. of cancel button tags:", noOfCancelBtnTags)
time.sleep(1)
cancelBtnTagName = footer.find_element(By.CSS_SELECTOR, "a")
tagNameForCancelBtn = cancelBtnTagName.tag_name
print("Tag name of cancel button:", tagNameForCancelBtn)
time.sleep(1)
continueBtnTagName = footer.find_element(By.CSS_SELECTOR, "input")
tagNameForContinueBtn = continueBtnTagName.tag_name
print("Tag name of continue button:", tagNameForContinueBtn)
time.sleep(1)
continueBtnTag = footer.find_elements(By.CSS_SELECTOR, "input")
noOfContinueBtnTags = len(continueBtnTag)
print("No. of continue button tags:", noOfContinueBtnTags)
time.sleep(1)
print("No. of buttons present in the footer:", noOfCancelBtnTags + noOfContinueBtnTags)
totalNoOfButtons = noOfCancelBtnTags + noOfContinueBtnTags
expectedNoOfButtonsInTheFooter = 2
time.sleep(1)
if totalNoOfButtons == expectedNoOfButtonsInTheFooter:
    print("Test case 20: Passed")
else:
    print("Test case 20: Failed")
time.sleep(1)
continueBtnBackgroundColor = continueBtnTagName.value_of_css_property('background-color')
continueBtnExpectedBackgroundColor = "rgba(255, 255, 255, 1)"
assert continueBtnExpectedBackgroundColor in continueBtnBackgroundColor
print("Background color of continue button:", continueBtnBackgroundColor)
time.sleep(1)
continueBtnColor = continueBtnTagName.value_of_css_property('color')
continueBtnExpectedColor = "rgba(226, 35, 26, 1)"
assert continueBtnExpectedColor in continueBtnColor
print("Color of continue button:", continueBtnColor)
time.sleep(1)
time.sleep(5)
driver.quit()
