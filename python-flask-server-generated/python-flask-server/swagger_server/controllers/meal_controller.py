import connexion
import six

from swagger_server.models.meal import Meal  # noqa: E501
import uuid
from swagger_server import util
from swagger_server.encoder import JSONEncoder
from flask import Response, make_response, jsonify
import swagger_server.controllers.utils as Nutrionix
mealid_body={}
meals=[]

def add_meal(body):  # noqa: E501
    """Add meal

    This can only be done by the logged in user. # noqa: E501

    :param body: Meal object to Add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Meal.from_dict(connexion.request.get_json())  # noqa: E501

        if(body.food_name in meals):
            return "Meal already in the list"
        if(not body.meal_id):
            #find meal_id
            body.meal_id=str(uuid.uuid4())
        try:
            if(not body.calorie):
                body.calorie=int(Nutrionix.nutrionix_calorie(body.food_name))
        except Exception as e:
            print("API errror occured with an error"+str(e))

        mealid_body[body.meal_id]=body
        meals.append(body.food_name)
        print(mealid_body)
    return "Added meal with id:"+body.meal_id


def delete_meal(meal_id):  # noqa: E501
    """Delete meal entry

    This can only be done by the logged in user. # noqa: E501

    :param meal_id: The meal that needs to be deleted.
    :type meal_id: str

    :rtype: None
    """
    if(meal_id not in mealid_body):
        #throw error
        print(meal_id)
        print(mealid_body)
        return make_response("MEAL not found!!!!",404)
    name=mealid_body[meal_id].food_name
    del mealid_body[meal_id]
    meals.remove(name)
    return make_response('meal deleted',200)


def get_meal_by_meal_id(meal_id):  # noqa: E501
    """Get meal by meal id

    Get Meal by specifying the meal ID # noqa: E501

    :param meal_id: The meal that needs to be fetched.
    :type meal_id: str

    :rtype: Meal
    """
    if(meal_id in mealid_body):
        return make_response(jsonify(mealid_body[meal_id]),200)
    return make_response("Meal id not found",400)


def update_meal(meal_id, body):  # noqa: E501
    """Update Meal entry

    This can only be done by the logged in user. # noqa: E501

    :param meal_id: meal that needs to be updated
    :type meal_id: str
    :param body: Updated meal object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Meal.from_dict(connexion.request.get_json())  # noqa: E501


    if(meal_id not in mealid_body):
        return make_response("Invalid meal",400)
    else:
        mealid_body[meal_id]=body
        return 'updated meal'
