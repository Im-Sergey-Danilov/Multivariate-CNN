import pandas as pd
import CNN


def get_data_of_bearings(class_number):
    dataframe = pd.read_excel('description_of_data.xlsx')
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(dataframe)

    list_of_rows = dataframe.values.tolist()

    axial_force = 0
    radial_force = 0
    revolutions = 0
    for each in list_of_rows:
        if int(class_number) in each:
            axial_force, radial_force = each[0], each[1]

    for i in range(2, 9):
        if i != 2:
            df1 = dataframe[['Unnamed: ' + str(i)]]
        else:
            df1 = dataframe[['Revolutions per minute']]

        list_of_columns = df1.values.tolist()
        for each in list_of_columns:
            if int(class_number) == each[0]:
                a = df1.iloc[0]
                a = a.values.tolist()
                revolutions = a[0]
    print("Spectrogram data is:")
    print("Axial force = {}, Radial force = {}, Revolutions = {}".format(axial_force, radial_force, revolutions))
    return revolutions


# # df_test = dataframe[['Unnamed: 2']]
# # print(df_test)

