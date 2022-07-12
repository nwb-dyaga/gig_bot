
def get_or_create(session, model, defaults, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        for key in defaults.keys():
            setattr(instance, key, defaults[key])
        session.commit()
        return instance
    else:
        instance = model(**kwargs)
        for key in defaults.keys():
            setattr(instance, key, defaults[key])
        session.add(instance)
        session.commit()
        return instance