from django import forms

from src.tasks import common_data


def get_form_by_number(task_id: int):
    match task_id:
        case 1:
            return Task01Form
        case 2:
            return Task02Form
        case 4:
            return Task04Form
        case _:
            return None


def get_params_by_number(task_id: int, form: forms.Form):
    match task_id:
        case 1:
            return {
                'A': common_data.SOLE.get_SOLE_by_name(form.data['matrix_name'])[0].tolist(),
                'b': common_data.SOLE.get_SOLE_by_name(form.data['matrix_name'])[1].tolist(),
                'delta': form.data['delta']
            }
        case 2:
            return {
                'A': common_data.SOLE.get_SOLE_by_name(form.data['sole_name'])[0].tolist(),
                'b': common_data.SOLE.get_SOLE_by_name(form.data['sole_name'])[1].tolist(),
            }
        case 4:
            return {
                'A': common_data.SOLE.get_SOLE_by_name(form.data['sole_name'])[0].tolist(),
                'b': common_data.SOLE.get_SOLE_by_name(form.data['sole_name'])[1].tolist(),
                'epsilon': form.data['epsilon']
            }
        case _:
            return None


class Task01Form(forms.Form):
    matrix_name = forms.ChoiceField(label='Выберите матрицу для исследования:',
                                    choices=common_data.SOLE.get_available_matrices_names())
    delta = forms.FloatField(
        label='Введите δ', min_value=0, max_value=1, initial=0.001)


class Task02Form(forms.Form):
    sole_name = forms.ChoiceField(label='Выберите СЛАУ для исследования:',
                                  choices=common_data.SOLE.get_available_matrices_names())


class Task04Form(forms.Form):
    sole_name = forms.ChoiceField(label='Выберите матрицу для исследования:',
                                  choices=common_data.SOLE.get_available_matrices_names())
    epsilon = forms.FloatField(
        label='Введите ε', min_value=0, max_value=1, initial=0.001)
