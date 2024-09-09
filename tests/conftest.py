import pytest
from faker import Faker
from pages.auth_page import AuthPage
from pages.home_page import HomePage
from pages.contact_us_page import ContactUsPage
from pages.test_cases_page import TCasesPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from typing import Generator, Dict
import random

@pytest.fixture
def home_page(new_page) -> HomePage:
    page = HomePage(new_page)
    return page

@pytest.fixture
def auth_page(new_page) -> AuthPage:
    page = AuthPage(new_page)
    return page

@pytest.fixture
def contact_us_page(new_page) -> ContactUsPage:
    page = ContactUsPage(new_page)
    return page

@pytest.fixture
def test_cases_page(new_page) -> TCasesPage:
    page = TCasesPage(new_page)
    return page

@pytest.fixture
def products_page(new_page) -> ProductsPage:
    page = ProductsPage(new_page)
    return page

@pytest.fixture
def cart_page(new_page) -> CartPage:
    page = CartPage(new_page)
    return page

@pytest.fixture
def checkout_page(new_page) -> CheckoutPage:
    page = CheckoutPage(new_page)
    return page
 
@pytest.fixture
def payment_page(new_page) -> PaymentPage:
    page = PaymentPage(new_page)
    return page
 
@pytest.fixture(name="username")
def faker_name() -> str:
    fake = Faker()
    return fake.name()

@pytest.fixture(name="email")
def faker_email() -> str:
    fake = Faker()
    return fake.email()

@pytest.fixture(name="password")
def faker_password() -> str:
    fake = Faker()
    return fake.password()

@pytest.fixture(name="first_name")
def faker_first_name() -> str:
    fake = Faker()
    return fake.first_name()

@pytest.fixture(name="last_name")
def faker_last_name() -> str:
    fake = Faker()
    return fake.last_name()

@pytest.fixture(name="company_name")
def faker_company_name() -> str:
    fake = Faker()
    return fake.company()

@pytest.fixture(name="address")
def faker_address() -> str:
    fake = Faker()
    return fake.address()

@pytest.fixture(name="address2")
def faker_address2() -> str:
    fake = Faker()
    return fake.secondary_address()

@pytest.fixture(name="state")
def faker_state() -> str:
    fake = Faker("en_US")
    return fake.state()

@pytest.fixture(name="city")
def faker_city() -> str:
    fake = Faker()
    return fake.city()

@pytest.fixture(name="zipcode")
def faker_zipcode() -> str:
    fake = Faker()
    return fake.postcode()

@pytest.fixture(name="mobile_number")
def faker_mobile_number() -> str:
    fake = Faker()
    return fake.phone_number()

@pytest.fixture(name="card_number")
def faker_card_number() -> str:
    fake = Faker()
    return fake.credit_card_number()

@pytest.fixture(name="cvc_code")
def faker_cvc_code() -> str:
    fake = Faker()
    return fake.credit_card_security_code()

@pytest.fixture(name="expiration_date")
def faker_expiration_date() -> str:
    fake = Faker()
    expiration_date  = fake.credit_card_expire(date_format="%m/%y")
    expiration_month, expiration_year = expiration_date.split('/')
    date = {
        "month": expiration_month,
        "year": expiration_year
    }
    return date

@pytest.fixture(name="subject")
def generate_subject() -> str:
    subjects = [
        "General Inquiry",
        "Product Support",
        "Billing Issue",
        "Feedback",
        "Job Application"
    ]
    return random.choice(subjects)

@pytest.fixture(name="message")
def faker_lorem() -> str:
    fake = Faker()
    return fake.paragraph(nb_sentences=1)

@pytest.fixture
def valid_login_creds(
    home_page: HomePage,
    auth_page: AuthPage,
    username: str,
    email: str,
    password: str,
    first_name: str,
    last_name: str,
    company_name: str,
    address: str,
    address2: str,
    state: str,
    city: str,
    zipcode: str,
    mobile_number: str,
) -> Generator[Dict[str, str], None, None]:
    creds = {
        "username": username,
        "email": email,
        "password": password,
        "first_name": first_name,
        "last_name": last_name,
        "company": company_name,
        "address": address,
        "address2": address2,
        "state": state,
        "city": city,
        "zipcode": zipcode,
        "mobile_number": mobile_number,
    }

    home_page.click_sign_up_login_btn()
    auth_page.signUp(creds["username"], creds["email"])
    auth_page.fill_account_info(creds["password"])
    auth_page.fill_adress_info(
        creds["first_name"],
        creds["last_name"],
        creds["company"],
        creds["address"],
        creds["address2"],
        creds["state"],
        creds["city"],
        creds["zipcode"],
        creds["mobile_number"],
    )
    auth_page.click_continue_btn()
    home_page.click_logout_btn()
    home_page.click_home_btn()
    yield creds
