import typing
def calculate_average_for_fold(fold_data: typing.Dict[str, typing.Union[typing.Optional[float], typing.List[float]]],
                               model_names: typing.List[str]) -> None:
    model_1_sum = 0
    model_2_sum = 0

    for dat in fold_data:
        model_1_sum += dat[model_names[0]]/len(fold_data)
        model_2_sum += dat[model_names[1]]/len(fold_data)

    print("Model {} average: {}".format(model_names[0], model_1_sum))
    print("Model {} average: {}".format(model_names[1], model_2_sum))