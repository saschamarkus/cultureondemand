from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from cultureondemand.models import Offer
from cultureondemand.extensions import ma, db
from cultureondemand.commons.pagination import paginate


class OfferSchema(ma.ModelSchema):

    id = ma.Int(dump_only=True)

    class Meta:
        model = Offer
        sqla_session = db.session


class OfferResource(Resource):
    """Single object resource

    ---
    get:
      tags:
        - api
      parameters:
        - in: path
          name: offer_id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  offer: OfferSchema
        404:
          description: offer does not exists
    put:
      tags:
        - api
      parameters:
        - in: path
          name: offer_id
          schema:
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              OfferSchema
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: offer updated
                  offer: OfferSchema
        404:
          description: offer does not exists
    delete:
      tags:
        - api
      parameters:
        - in: path
          name: offer_id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: offer deleted
        404:
          description: offer does not exists
    """

    # method_decorators = [jwt_required]

    def get(self, offer_id):
        schema = OfferSchema()
        offer = Offer.query.get_or_404(offer_id)
        return {"offer": schema.dump(offer)}

    def put(self, offer_id):
        schema = OfferSchema(partial=True)
        offer = Offer.query.get_or_404(offer_id)
        offer = schema.load(request.json, instance=offer)

        db.session.commit()

        return {"msg": "offer updated", "offer": schema.dump(offer)}

    def delete(self, offer_id):
        offer = Offer.query.get_or_404(offer_id)
        db.session.delete(offer)
        db.session.commit()

        return {"msg": "offer deleted"}


class OfferList(Resource):
    """Creation and get_all

    ---
    get:
      tags:
        - api
      responses:
        200:
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginatedResult'
                  - type: object
                    properties:
                      results:
                        type: array
                        items:
                          $ref: '#/components/schemas/OfferSchema'
    post:
      tags:
        - api
      requestBody:
        content:
          application/json:
            schema:
              OfferSchema
      responses:
        201:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: offer created
                  offer: OfferSchema
    """

    #method_decorators = [jwt_required]

    def get(self):
        schema = OfferSchema(many=True)
        query = Offer.query
        return paginate(query, schema)

    def post(self):
        schema = OfferSchema()
        offer = schema.load(request.json)

        db.session.add(offer)
        db.session.commit()

        return {"msg": "offer created", "offer": schema.dump(offer)}, 201
