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
        case 5:
            return Task05Form
        case 6:
            return Task06Form
        case 7:
            return Task06Form
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
        case 5:
            return {
                'A': common_data.SOLE.get_SOLE_by_name(form.data['sole_name'])[0].tolist(),
                'x_0': form.data['x_0'].split(','),
                'epsilon': form.data['epsilon']
            }
        case 6:
            return {
                'A': common_data.SOLE.get_SOLE_by_name(form.data['sole_name'])[0].tolist(),
                'epsilon': form.data['epsilon']
            }
        case 7:
            return {
                'A': common_data.SOLE.get_SOLE_by_name(form.data['sole_name'])[0].tolist(),
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


class Task05Form(forms.Form):
    sole_name = forms.ChoiceField(label='Выберите матрицу для исследования:',
                                  choices=common_data.SOLE.get_available_matrices_names())
    x_0 = forms.CharField(
        label='Введите начальное приближение. Обратите внимание на длину вектора!', initial='0,1.25,555,4.4', widget=forms.TextInput(attrs={'class': 'float-list'}))
    epsilon = forms.FloatField(
        label='Введите ε', min_value=0.00001, max_value=0.01, initial=0.001)


class Task06Form(forms.Form):
    sole_name = forms.ChoiceField(label='Выберите матрицу для исследования:',
                                  choices=common_data.SOLE.get_available_matrices_names())
    epsilon = forms.FloatField(
        label='Введите ε', min_value=0.00001, max_value=0.01, initial=0.001)


class Task07Form(forms.Form):
    sole_name = forms.ChoiceField(label='Выберите матрицу для исследования:',
                                  choices=common_data.SOLE.get_available_matrices_names())
    epsilon = forms.FloatField(
        label='Введите ε', min_value=0.00001, max_value=0.01, initial=0.001)
