import csv
import pandas as pd
from updatedb.models import Character, Weapon, Artifact_set


def pause():
    print("-"*70)


def update_db(csv_file):
    file = open(f'updatedb/scripts/csvs/{csv_file}.csv')
    read_file = csv.reader(file)

    return read_file


def clear_data():
    Character.objects.all().delete()
    Artifact_set.objects.all().delete()
    Weapon.objects.all().delete()
    print("Deleted previous version of db")


def get_weapons(url, weapon_type):
    df = pd.read_html(url)[1]
    df = df[['Name', 'Base ATK (Max)', '2nd Stat (Max)', 'Passive Ability']]
    df.to_csv(f'updatedb/scripts/csvs/{weapon_type}.csv')
    print(f"Getting {weapon_type}s - Done")
    pause()


def get_characters(url):
    df = pd.read_html(url)[2]
    df = df[['Name', 'Weapon', 'Element']]
    df.to_csv('updatedb/scripts/csvs/Character.csv')
    print("Collecting characters - Done")
    pause()


def get_artifacts(url):
    df = pd.read_html(url)[1]
    df = df.loc[df['Rarity'] == "4-5★"]
    df[['2 Piece', '4 Piece']] = df.Bonuses.str.split('4 Piece:', expand=True)
    df = df[['Set', '2 Piece', '4 Piece']]
    df['2 Piece'] = df['2 Piece'].str.replace('2 Piece:', '')
    df = df.sort_values(by='Set', ignore_index=True)
    df.to_csv('updatedb/scripts/csvs/Artifacts.csv')
    print("Collecting artifacts - Done")
    pause()


def update_characters():
    read_file = update_db("Character")

    count = 1

    for item in read_file:
        if count == 1:
            pass
        else:
            Character.objects.create(name=item[1], weapon=item[2], vision=item[3])
        count += 1
    print("Updating characters - Done")


def update_artifacts():
    read_file = update_db("Artifacts")

    count = 1

    for item in read_file:
        if count == 1:
            pass
        else:
            Artifact_set.objects.create(name=item[1], piece_2=item[2], piece_4=item[3])
        count += 1
    print("Updating Artifacts - Done")


def update_weapons(csv_file):
    read_file = update_db(csv_file)

    count = 1

    for item in read_file:
        if count == 1:
            pass
        else:
            Weapon.objects.create(name=item[1], type=csv_file, atk=item[2], stat=item[3], ability=item[4])
        count += 1
    print(f"Updating {csv_file}s - Done")


def make_csv():
    get_weapons("https://genshin-impact.fandom.com/wiki/Sword", "Sword")
    get_weapons("https://genshin-impact.fandom.com/wiki/Claymore", "Claymore")
    get_weapons("https://genshin-impact.fandom.com/wiki/Polearm", "Polearm")
    get_weapons("https://genshin-impact.fandom.com/wiki/Bow", "Bow")
    get_weapons("https://genshin-impact.fandom.com/wiki/Catalyst", "Catalyst")

    get_characters('https://genshin-impact.fandom.com/wiki/Characters')

    get_artifacts("https://genshin-impact.fandom.com/wiki/Artifacts/Sets")
    print('Created csv files')


def run():
    clear_data()
    pause()
    make_csv()
    update_characters()
    update_artifacts()
    update_weapons("Sword")
    update_weapons("Claymore")
    update_weapons("Polearm")
    update_weapons("Bow")
    update_weapons("Catalyst")
    print("Updated database")



