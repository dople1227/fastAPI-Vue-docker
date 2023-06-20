def test_ping(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "Ping Pong!"}


def test_get_model(test_app):
    modelName = "lenet"
    response = test_app.get(f"/models/{modelName}")
    print("\nBefore response", end="\n")
    print("\n" + str(response.json()), end="\n")
    print("\nAfter response", end="\n")
    assert response.json() == {"model_name": "lenet", "message": "LeCNN all the images"}

