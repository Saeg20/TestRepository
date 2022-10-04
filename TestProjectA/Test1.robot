*** Settings ***

Library  SeleniumLibrary

*** Variables ***



*** Keywords ***



*** Test Cases ***
TC01 Opening a browser in chrome

   Open Browser    https://www.nu.nl    chrome
   sleep      5s
   Close Browser
