def process_user_data(user_id):
    user = get_user_from_cache(user_id)
    if not user:
        return None
    return user.get('profile')  # This will trigger the test error

def get_user_from_cache(user_id):
    # Simulate cache miss
    return None
