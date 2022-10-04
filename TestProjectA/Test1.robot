*** Settings ***

Library  SeleniumLibrary

*** Variables ***



*** Keywords ***



*** Test Cases ***
TC01 Opening a browser

   Open Browser    https://www.nu.nl    chrome
   sleep      5s
   Close Browser
