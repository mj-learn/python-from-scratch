def process_data(data):
    try:
        if not data:
            raise ValueError("No data to process.")
        # Process the data
    except ValueError as e:
        print(f"Problem processing data: {e}")
        raise  # Re-raising the exception


try:
    process_data(None)
except ValueError as e:
    print(f"Error: {e}")
