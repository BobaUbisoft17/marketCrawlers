from pydantic_core import from_json
import requests
import uuid
from models import * 

class LentaParser:
    
    __session_token : str
    __device_id: str

    def __init__(self, marketing_partner_key: str) -> None:
        self.marketing_partner_key = marketing_partner_key

    def get_session_token(self) -> str:
        return self.__session_token

    def update_session_token(self) -> None:
        self.__device_id = str(uuid.uuid4())
        self.__session_token = self.fetch_session_token() 

    def get_region_list(self) -> list[City]:
        # нужно сделать аналог ретрая
        regions = RegionList.model_validate(from_json(
            requests.post(
                url="https://lenta.com/api/rest/regionList",
                data=self.create_request_body("regionList").model_dump_json()
            ).json()
        ))

        return regions.body.cities

    def get_stores(self) -> None:
        ...

    def set_store_id_in_session(self) -> None:
        ...

    def get_categories(self) -> None:
        ...

    def get_items_by_category_id(self) -> None:
        ...

    def fetch_session_token(self) -> str:
        res = Token.model_validate(from_json(
                requests.post(
                    url="https://lenta.com/api/rest/sessionGet",
                    headers=self.create_request_headers("application/json").model_dump(),
                    data=self.create_request_body("sessionGet").model_dump_json(),
                ).text
            ))
        # Добовить логирование на соотвествие токенов в ответе и названия сервера
        return res.body.session_token 

    def create_request_body(
            self,
            method_name: str
    ) -> Body:
        return Body(
                request=Head(
                    head=Body(
                        marketing_partner_key=self.marketing_partner_key,
                        method_name=method_name,
                        device_id=self.__device_id,
                        session_token=self.get_session_token()
                    )
                )
            )

    def create_request_headers(self, content_type: str) -> Headers:
        # Возможно стоит пихать просто фейкого юзерагента, чтобы это было хоть как-то нормально
        return Headers(
                content_type=content_type,
        )


lenta = LentaParser("mp80-661295c9cbf9d6b2f6428414504a8deed3020641")
lenta.fetch_session_token()
