# 🔐 Selenium Login Checker

This script automates login attempts for multiple accounts using [Selenium WebDriver](https://www.selenium.dev/). It reads account credentials from a text file, attempts to log in through a specified website, and saves valid accounts to a file.

## ⚠️ Disclaimer

> **This tool is for educational and testing purposes only.**  
> Do not use this script to attempt unauthorized access to websites. Make sure you have permission to automate or test the login functionality on the target site.

## 📂 How It Works

1. Reads credentials from `accounts.txt` in the format `username:password`.
2. For each account:
   - Opens the login page in Chrome.
   - Enters the credentials.
   - Clicks the login button.
   - Waits for an invalid login message.
   - Logs valid accounts into `valid.txt`.

## 🛠️ Setup

### 1. Install Requirements

```bash
pip install selenium
```

Make sure you have [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) installed and it's in your system path.

### 2. Prepare `accounts.txt`

Example:

```
user1@example.com:password123
user2@example.com:qwerty
```

### 3. Update the Script

Replace each `'CHANGETHIS'` with the **full XPath** of the respective HTML elements on your target login page:

```python
usernameInput = driver.find_element(By.XPATH, 'FULL_XPATH_HERE')
```

Also, set the login page URL:

```python
url = "https://example.com/login"
```

## ✅ Output

- Valid accounts will be saved to `valid.txt`
- Console output will display `[VALID]` or `[INVALID]` for each login attempt.

## 🧪 Example Snippet

```python
WebDriverWait(driver, 2).until(
    EC.presence_of_element_located((By.XPATH, 'FULL_XPATH_OF_ERROR_MESSAGE'))
)
```

If the error message appears within 2 seconds, the account is considered **invalid**.

## 📌 Notes

- Make sure the login form is visible before interacting with it.
- Increase the wait time if the page loads slowly.
- For large-scale testing, consider running the browser in **headless** mode.

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
