import httpx
import pytest
import pdb

@pytest.mark.asyncio
async def test_sign_new_user(default_client: httpx.AsyncClient) -> None: 
    pdb.set_trace()   
    payload = {"email": "test@test.com", "password": "testpassword"}

    headers = {"accept": "application/json", "Content-type": "application/json"}

    test_response = {"message": "사용자가 등록되었습니다."}

    response = await default_client.post("/user/signup", json=payload, headers=headers)    
    assert response.status_code == 200
    assert response.json() == test_response


@pytest.mark.asyncio
async def test_sign_user_in(default_client: httpx.AsyncClient) -> None:
    pdb.set_trace()   
    payload = {"username": "test@test.com", "password": "testpassword"}

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    response = await default_client.post("/user/signin", data=payload, headers=headers)
    assert response.status_code == 200
    assert response.json()["token_type"] == "Bearer"
