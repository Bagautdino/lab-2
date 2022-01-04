import pandas as pd
import requests as req


def find_anime_by_name(df):
    name = input(str('Напишите название анимэ?\nЕсли это не конкретное анимэ ENTER: '))
    if name != '':
        for anime_name in range(len(df['Name'])):
            if (df['Name'][anime_name]).lower() == name.lower() or \
                    df['Alternative Name'][anime_name].lower() == name.lower():
                print(df['Name'][anime_name] + '\n' + df['Url'][anime_name])
                quit()
        print('Такого аниме не найдено')
        quit()


def find_anime_by_tag(df, collection_anime):
    tags = str(input('Какой жанр Вас интересует?\n(Введите через запятую, если это не очень важно нажмите ENTER): '))
    if tags != '':
        tags_array = tags.split(',')
        for tag in tags_array:
            for tag_count in range(len(df['Tags'])):
                if tag.lower() in df['Tags'][tag_count].lower():
                    collection_anime.append(df.loc[tag_count, :])
        if len(collection_anime) == 0:
            print('Таких жанров не найдено')
            quit()


def find_anime_by_episodes(df, collection_anime):
    episodes = str(input('Вас интересует короткометражное или полнометражное аниме?\n(ENTER, если не важно): '))
    if episodes != '':
        tmp_anime = collection_anime[:] if len(collection_anime) else df
        collection_anime.clear()
        for anime in tmp_anime:
            if episodes.lower() == 'короткометражное':
                if anime['Episodes'] == 'Unknown':
                    continue
                if int(anime['Episodes']) > 1:
                    collection_anime.append(anime)
            elif episodes.lower() == 'полнометражное':
                if anime['Episodes'] == '1':
                    collection_anime.append(anime)
        if len(collection_anime) < 1:
            print('Таких аниме не найдено')
            quit()


def find_anime_by_duration(df, collection_anime):
    duration = str(input('Какая продолжительность Вас интересует (Кол-во часов)?\n(ENTER, если не важно): '))
    if duration != '':
        tmp_anime = collection_anime[:] if len(collection_anime) else df
        collection_anime.clear()
        for anime in tmp_anime:
            if anime['Duration'] == 'Unknown':
                continue
            if anime['Duration'] == duration:
                collection_anime.append(anime)
        if len(collection_anime) < 1:
            print('Таких аниме не найдено')
            quit()


def rate_sorting(collection_anime):
    rating_data = []
    for anime in collection_anime:
        if anime['Rating Score'] == 'Unknown':
            continue
        else:
            rating_data.append(float(anime['Rating Score']))
    rating_data = list(set(rating_data))
    rating_data.sort()
    rating_data.reverse()
    tmp_anime = collection_anime
    collection_anime = []
    for score in rating_data:
        for anime in tmp_anime:
            if anime['Rating Score'] == 'Unknown':
                continue
            if score == float(anime['Rating Score']):
                collection_anime.append(anime)
        for anime in tmp_anime:
            if anime['Rating Score'] == 'Unknown':
                collection_anime.append(anime)
    return collection_anime


def main():
    collection_anime = []
    df = pd.read_csv('anime.csv')
    find_anime_by_name(df)
    find_anime_by_tag(df, collection_anime)
    find_anime_by_episodes(df, collection_anime)
    find_anime_by_duration(df, collection_anime)
    if len(collection_anime) > 0:
        rate_sorting(collection_anime)
        df_good = pd.DataFrame(collection_anime)
        df_good.to_json('out.json')

        for anime in collection_anime[:5]:
            url = str('https://www.anime-planet.com/images/anime/covers/'
                      + str(anime['Anime-PlanetID']) + '.jpg?t=1523213250')
            name = str(anime['Anime-PlanetID'])
            img = req.get(url)
            img_opt = open(name + '.jpg', 'wb')
            img_opt.write(img.content)
            img_opt.close()
        return
    print('Вам подходят все аниме')


if __name__ == '__main__':
    main()
