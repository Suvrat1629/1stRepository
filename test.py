def process_user_data(user_id):
    user = get_user_from_cache(user_id)  # Returns None
    if not user:
        return None
    return user.get('profile')  # ❌ This line will crash with AttributeError
