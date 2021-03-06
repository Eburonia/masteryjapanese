''' Tenses '''


from verb_table_shifter import verb_table_shifter
from te_form_generator import te_form
from verbs import verbs


# Present Polite Positive
def present_polite_positive(verb):

    ''' Present Polite Positive '''

    # Declare English, Hiragana, Mazegaki
    list_ = ['', '', '']

    # Get the verb type (ru/u)
    type_ = verbs[verb]['verb-type']

    # When 'ru' verb
    if type_ == 'ru':

        # Return English
        list_[0] = verbs[verb]['present_en'] + ' (polite)'

        # Return Hiragana
        list_[1] = verbs[verb]['hiragana'][:-1] + 'ます'

        # Return Mazegaki (Kanji + Hiragana)
        list_[2] = verb[:-1] + 'ます'

        return list_

    # When 'u' verb
    elif type_ == 'u':

        # Return English
        list_[0] = verbs[verb]['present_en'] + ' (polite)'

        # Return Hiragana
        list_[1] = verbs[verb]['hiragana'][:-1] + verb_table_shifter(
                                                    verb, 2) + 'ます'

        # Return Mazegaki (Kanji + Hiragana)
        list_[2] = verb[:-1] + verb_table_shifter(verb, 2) + 'ます'

        return list_

    # When not 'ru' or 'u' verb
    else:

        return 'ERROR 6'


# Present Polite Negative
def present_polite_negative(verb):

    ''' Present Polite Negative '''

    # Declare Hiragana and Mazegaki
    list_ = ['', '', '']

    # Get the verb type (ru/u)
    type_ = verbs[verb]['verb-type']

    # When 'ru' verb
    if type_ == 'ru':

        # Return English
        list_[0] = 'not ' + verbs[verb]['present_en'] + ' (polite)'

        # Return Hiragana
        list_[1] = verbs[verb]['hiragana'][:-1] + 'ません'

        # Return Mazegaki (Kanji + Hiragana)
        list_[2] = verb[:-1] + 'ません'

        return list_

    # When 'u' verb
    elif type_ == 'u':

        # Return English
        list_[0] = 'not ' + verbs[verb]['present_en'] + ' (polite)'

        # Return Hiragana
        list_[1] = verbs[verb]['hiragana'][:-1] + verb_table_shifter(
                                                    verb, 2) + 'ません'

        # Return Mazegaki (Kanji + Hiragana)
        list_[2] = verb[:-1] + verb_table_shifter(verb, 2) + 'ません'

        return list_

    # When not 'ru' or 'u' verb
    else:

        return 'ERROR 7'


# Past Polite Positive
def past_polite_positive(verb):

    ''' Past Polite Positive '''

    # Declare Hiragana and Mazegaki
    list_ = ['', '', '']

    # Get the verb type (ru/u)
    type_ = verbs[verb]['verb-type']

    # When 'ru' verb
    if type_ == 'ru':

        # Return English
        list_[0] = verbs[verb]['past_en'] + ' (polite)'

        # Return Hiragana
        list_[1] = verbs[verb]['hiragana'][:-1] + 'ました'

        # Return Mazegaki (Kanji + Hiragana)
        list_[2] = verb[:-1] + 'ました'

        return list_

    # When 'u' verb
    elif type_ == 'u':

        # Return English
        list_[0] = verbs[verb]['past_en'] + ' (polite)'

        # Return Hiragana
        list_[1] = verbs[verb]['hiragana'][:-1] + verb_table_shifter(
                                                    verb, 2) + 'ました'

        # Return Mazegaki (Kanji + Hiragana)
        list_[2] = verb[:-1] + verb_table_shifter(verb, 2) + 'ました'

        return list_

    # When not 'ru' or 'u' verb
    else:

        return 'ERROR 8'


# Past Polite Negative
def past_polite_negative(verb):

    ''' Past Polite Negative '''

    # Declare Hiragana and Mazegaki
    list_ = ['', '', '']

    # Get the verb type (ru/u)
    type_ = verbs[verb]['verb-type']

    # When 'ru' verb
    if type_ == 'ru':

        # Return English
        list_[0] = 'not ' + verbs[verb]['past_en'] + ' (polite)'

        # Return Hiragana
        list_[1] = verbs[verb]['hiragana'][:-1] + 'ませんでした'

        # Return Mazegaki (Kanji + Hiragana)
        list_[2] = verb[:-1] + 'ませんでした'

        return list_

    # When 'u' verb
    elif type_ == 'u':

        # Return English
        list_[0] = 'not ' + verbs[verb]['past_en'] + ' (polite)'

        # Return Hiragana
        list_[1] = verbs[verb]['hiragana'][:-1] + verb_table_shifter(
                                                verb, 2) + 'ませんでした'

        # Return Mazegaki (Kanji + Hiragana)
        list_[2] = verb[:-1] + verb_table_shifter(verb, 2) + 'ませんでした'

        return list_

    # When not 'ru' or 'u' verb
    else:

        return 'ERROR 9'


# Present Plain Positive
def present_plain_positive(verb):

    ''' Present Plain Positive '''

    # Declare Hiragana and Mazegaki
    list_ = ['', '', '']

    # Return English
    list_[0] = verbs[verb]['present_en'] + ' (plain)'

    # Return Hiragana
    list_[1] = verbs[verb]['hiragana']

    # Return Mazegaki (Kanji + Hiragana)
    list_[2] = verb

    return list_


# Present Plain Negative
def present_plain_negative(verb):

    ''' Present Plain Negative '''

    # Declare Hiragana and Mazegaki
    list_ = ['', '', '']

    # Get the verb type (ru/u)
    type_ = verbs[verb]['verb-type']

    # When 'ru' verb
    if type_ == 'ru':

        # Return English
        list_[0] = 'not ' + verbs[verb]['present_en'] + ' (plain)'

        # Return Hiragana
        list_[1] = verbs[verb]['hiragana'][:-1] + 'ない'

        # Return Mazegaki (Kanji + Hiragana)
        list_[2] = verb[:-1] + 'ない'

        return list_

    # When 'u' verb
    elif type_ == 'u':

        # Return English
        list_[0] = 'not ' + verbs[verb]['present_en'] + ' (plain)'

        # Return Hiragana
        list_[1] = verb[:-1] + verb_table_shifter(verb, 1) + 'ない'

        # Return Mazegaki (Kanji + Hiragana)
        list_[2] = verbs[verb]['hiragana'][:-1] + verb_table_shifter(
                                                    verb, 1) + 'ない'

        return list_

    # When not 'ru' or 'u' verb
    else:

        return 'ERROR 10'


# Past Plain Positive
def past_plain_positive(verb):

    ''' Past Plain Positive '''

    # Declare Hiragana and Mazegaki
    list_ = ['', '', '']

    # Get the verb type (ru/u)
    type_ = verbs[verb]['verb-type']

    # When 'ru' verb
    if type_ == 'ru':

        # Return English
        list_[0] = verbs[verb]['past_en'] + ' (plain)'

        # Return Hiragana
        list_[1] = verbs[verb]['hiragana'][:-1] + 'た'

        # Return Mazegaki (Kanji + Hiragana)
        list_[2] = te_form(verb, 0)[:-1] + 'た'

        return list_

    # When 'u' verb
    elif type_ == 'u':

        # Return English
        list_[0] = verbs[verb]['past_en'] + ' (plain)'

        if te_form(verb, 0)[-1:] == 'て':

            list_[1] = te_form(verb, 0)[:-1] + 'た'
            list_[2] = te_form(verb, 1)[:-1] + 'た'

            return list_

        elif te_form(verb, 0)[-1:] == 'で':

            list_[1] = te_form(verb, 0)[:-1] + 'だ'
            list_[2] = te_form(verb, 1)[:-1] + 'だ'

            return list_

        else:

            return 'ERROR 11'

    else:

        return 'ERROR 12'


# Past Plain Negative
def past_plain_negative(verb):

    ''' Past Plain Negative '''

    # Declare Hiragana and Mazegaki
    list_ = ['', '', '']

    # Get the verb type (ru/u)
    type_ = verbs[verb]['verb-type']

    # When 'ru' verb
    if type_ == 'ru':

        # Return English
        list_[0] = 'not ' + verbs[verb]['past_en'] + ' (plain)'

        # Return Hiragana
        list_[1] = verbs[verb]['hiragana'][:-1] + 'なかった'

        # Return Mazegaki (Kanji + Hiragana)
        list_[2] = verb[:-1] + 'なかった'

        return list_

    # When 'u' verb
    elif type_ == 'u':

        # Return English
        list_[0] = 'not ' + verbs[verb]['past_en'] + ' (plain)'

        # Return Hiragana
        list_[1] = verb[:-1] + verb_table_shifter(verb, 1) + 'なかった'

        # Return Mazegaki (Kanji + Hiragana)
        list_[2] = verbs[verb]['hiragana'][:-1] + verb_table_shifter(
                                                    verb, 1) + 'なかった'

        return list_

    # When not 'ru' or 'u' verb
    else:

        return 'ERROR 13'


def present_polite_progressive_positive(verb):

    ''' Present Polite Progressive Positive '''

    # Declare Hiragana and Mazegaki
    list_ = ['', '']

    # Get the verb type (ru/u)
    type_ = verbs[verb]['verb-type']

    # When 'ru' verb
    if type_ == 'ru':

        # Return Hiragana
        list_[0] = te_form(verb, 1) + 'います'

        # Return Mazegaki (Kanji + Hiragana)
        list_[1] = te_form(verb, 0) + 'います'

        return list_

    # When 'u' verb
    elif type_ == 'u':

        # Return Hiragana
        list_[0] = te_form(verb, 1) + 'います'

        # Return Mazegaki (Kanji + Hiragana)
        list_[1] = te_form(verb, 0) + 'います'

        return list_

    # When not 'ru' or 'u' verb
    else:

        return 'ERROR 14'


def present_polite_progressive_negative(verb):

    ''' Present Polite Progressive Negative '''

    # Declare Hiragana and Mazegaki
    list_ = ['', '']

    # Get the verb type (ru/u)
    type_ = verbs[verb]['verb-type']

    # When 'ru' verb
    if type_ == 'ru':

        # Return Hiragana
        list_[0] = te_form(verb, 1) + 'います'

        # Return Mazegaki (Kanji + Hiragana)
        list_[1] = te_form(verb, 0) + 'います'

        return list_

    # When 'u' verb
    elif type_ == 'u':

        # Return Hiragana
        list_[0] = te_form(verb, 1) + 'いません'

        # Return Mazegaki (Kanji + Hiragana)
        list_[1] = te_form(verb, 0) + 'いません'

        return list_

    # When not 'ru' or 'u' verb
    else:

        return 'ERROR 15'


def past_polite_progressive_positive(verb):

    ''' Past Polite Progressive Positive '''

    # Declare Hiragana and Mazegaki
    list_ = ['', '']

    # Get the verb type (ru/u)
    type_ = verbs[verb]['verb-type']

    # When 'ru' verb
    if type_ == 'ru':

        # Return Hiragana
        list_[0] = te_form(verb, 1) + 'いました'

        # Return Mazegaki (Kanji + Hiragana)
        list_[1] = te_form(verb, 0) + 'いました'

        return list_

    # When 'u' verb
    elif type_ == 'u':

        # Return Hiragana
        list_[0] = te_form(verb, 1) + 'いました'

        # Return Mazegaki (Kanji + Hiragana)
        list_[1] = te_form(verb, 0) + 'いました'

        return list_

    # When not 'ru' or 'u' verb
    else:

        return 'ERROR 16'


def past_polite_progressive_negative(verb):

    ''' Past Polite Progressive Negative '''

    # Declare Hiragana and Mazegaki
    list_ = ['', '']

    # Get the verb type (ru/u)
    type_ = verbs[verb]['verb-type']

    # When 'ru' verb
    if type_ == 'ru':

        # Return Hiragana
        list_[0] = te_form(verb, 1) + 'いませんでした'

        # Return Mazegaki (Kanji + Hiragana)
        list_[1] = te_form(verb, 0) + 'いませんでした'

        return list_

    # When 'u' verb
    elif type_ == 'u':

        # Return Hiragana
        list_[0] = te_form(verb, 1) + 'いませんでした'

        # Return Mazegaki (Kanji + Hiragana)
        list_[1] = te_form(verb, 0) + 'いませんでした'

        return list_

    # When not 'ru' or 'u' verb
    else:

        return 'ERROR 17'
