from src.repositories.base_repository import Model, Schema


class BaseDataMapper:
    model: type[Model]
    schema: type[Schema]
    
    @classmethod
    def map_to_domain_entity(cls, data: Model) -> Schema:
        ''' Сериализация объекта модели в схему '''
        return cls.schema.model_validate(data)

    @classmethod
    def map_to_persistence_entity(cls, data: Schema) -> Model:
        ''' Сериализация схемы в объект модели '''
        return cls.model(**data.model_dump())