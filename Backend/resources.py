def get_resources(resource_type):
    # Dummy data for demonstration
    resources = {
        "therapist": [{"name": "Dr. John Doe", "contact": "123-456-7890"}],
        "support_group": [{"name": "Support Group A", "contact": "987-654-3210"}],
    }
    return resources.get(resource_type, resources["therapist"])
