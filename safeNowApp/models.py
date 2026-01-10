from datetime import datetime

from django.db import models
import bcrypt
import re


# Create your models here.
class UserManager(models.Manager):
    def basic_validator_login(self, postData):
        errors = {}
        user = User.objects.filter(email=postData['email'])
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Wrong email address!"
        if len(postData['email']) == 0:
            errors["emailrequired"] = "Email is required!"
        if len(postData['password']) == 0:
            errors["passwordrequired"] = "Password is required!"

        if not len(user):
            errors['emailnewuser'] = "Email or password is wrong"
        return errors

    def basic_validator_reg(self, postData):
        errors = {}
        current_year = datetime.now().year
        new_user = User.objects.filter(email=postData['email'])
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if len(postData['confirmpassword']) < 8:
            errors["confirmpassword"] = "Confirm Password should be at least 8 characters"
        if len(postData['lastname']) < 3:
            errors["lastname"] = "Last name should be at least 3 characters"
        if len(postData['firstname']) < 3:
            errors["firstname"] = "First Name should be at least 3 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Wrong email address!"
        if postData['password'] != postData['confirmpassword']:
            errors['password_confirm'] = "Password Dosent Match!"
        if len(postData['email']) == 0:
            errors["emailrequired"] = "Email is required!"
        if len(postData['password']) == 0:
            errors["passwordrequired"] = "Password is required!"
        if len(postData['confirmpassword']) == 0:
            errors["confirmpasswordrequired"] = "Confrim password is required!"
        if len(postData['lastname']) == 0:
            errors["lastnamerequired"] = "Last name is required!"
        if len(postData['firstname']) == 0:
            errors["firstnamerequired"] = "First name is required!"
        if len(new_user):
            errors['emailnewuser'] = "Email already exist"
        if len(postData['role']) == 0:
            errors["role"] = "Role is required"
        elif postData['role'] != "user" and postData['role'] != "volunteer":
            errors["role"] = "You can't use this role"
        elif postData['role'] == "volunteer":
            user_year = int(postData['DOB'][:4])
            if (current_year - user_year) < 18:
                errors['age'] = "You must be 18-year old to perform this action"
        return errors


    def basic_validator_volunteer(self, postData):
        errors = {}
        if postData["title"] == '' :
            errors["title"] = "Title is required"
        if postData["description"] == '' :
            errors["description"] = "Description is required"
        if postData["location"] == '' :
            errors["location"] = "Location is required"
        if postData["availability"] == '' :
            errors["availability"] = "Availability is required"
        if not "category" in postData:
            errors["category"] = "Category is required"
        return errors



class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    DOB = models.DateField()
    role = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_volunteer = models.BooleanField(default=False)
    objects = UserManager()


class CaseEmergencyManager(models.Manager):
    def emergency_validator(self, postData):
        errors = {}
        if postData["title"] == '':
            errors["title"] = "Title is required!"
        if not "category" in postData:
            errors["category"] = "Category is required!"
        if not "authorities" in postData:
            errors["authorities"] = "Authority is required!"
        if postData["location"] == '':
            errors["location"] = "Location is required!"
        if not "status" in postData:
            errors["status"] = "Status is required!"
        return errors


class CaseEmergency(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    long = models.FloatField()
    lat = models.FloatField()
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True)
    audio = models.FileField(upload_to='audio/', blank=True)
    authorities = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name="cases", on_delete=models.CASCADE)
    current_status = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='cases/', null=True, blank=True)
    qr_code = models.ImageField(upload_to='cases/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CaseEmergencyManager()


class Services(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    rating = models.IntegerField()
    owner = models.ForeignKey(User, related_name="services", on_delete=models.CASCADE)
    requested_by = models.ManyToManyField(User, related_name="requested")
    availability = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ServiceRating(models.Model):
    rating = models.IntegerField()
    user = models.ForeignKey(User, related_name="user_rating", on_delete=models.CASCADE)
    service = models.ForeignKey(Services,related_name="service_rating",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def get_users():
    return User.objects.all()


def get_user(id):
    return User.objects.get(id=id)


def create_user(post):
    user_password = post['password']
    hash1 = bcrypt.hashpw(user_password.encode(), bcrypt.gensalt()).decode()
    return User.objects.create(firstname=post['firstname'], lastname=post['lastname'], phonenumber=post['phonenumber'],
                               email=post['email'], password=hash1, DOB=post['DOB'], address=post['address'],
                               role=post['role'])


def login_user(post, session):
    user_exist = User.objects.filter(email=post['email'])
    if user_exist:
        logged_user = user_exist[0]
        if bcrypt.checkpw(post['password'].encode(), logged_user.password.encode()):
            session['user_id'] = logged_user.id
            return True
    return False


def create_case(post, image, audio_data, text_description,user,lat,long):
    return CaseEmergency.objects.create(title=post.get("title"),
                                        category=post.get("category"),
                                        authorities=post.get("authorities"),
                                        lat=lat,
                                        long=long,
                                        description=text_description,
                                        image=image,
                                        audio=audio_data,
                                        status=post.get("status"),
                                        current_status="PENDING",
                                        created_by=user)

def create_volunteer(postData):
    new_volunteer = User.objects.create(
        firstname=postData['firstname'],
        lastname=postData['lastname'],
        email=postData['email'],
        password=postData['password'],
        DOB=postData['DOB'],
        phone=postData['phone'],
        address=postData['address'],
        is_volunteer=True,
    )
    return new_volunteer

def cancel_volunteer(postData):
    volunteer = User.objects.get(id=postData['volunteer_id'])
    volunteer.is_volunteer = False
    volunteer.save()


def get_all_cases():
    return CaseEmergency.objects.all()

def get_case_by_id(id):
    return CaseEmergency.objects.get(id=id)

def get_all_services():
    return Services.objects.all()

def get_service_by_id(service_id):
    return Services.objects.get(id=service_id)

def rate_service(service_id, user_id,rate):
    service = get_service_by_id(service_id)
    user = get_user(user_id)
    return ServiceRating.objects.create(service=service, user=user, rating=rate)

def get_all_ratings():
    return ServiceRating.objects.all()

def create_service(title, description, location, category,availability,user):
    return Services.objects.create(title = title, description = description,location = location,category = category,owner=user,rating=0,availability = availability,status = "ACTIVE")


def service_request(service,user):
    service.status = "PENDING"
    service.save()
    return service.requested_by.add(user)

def delete_a_service(service_id):
    service = get_service_by_id(service_id)
    return service.delete()