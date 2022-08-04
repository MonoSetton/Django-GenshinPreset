import csv
import pandas as pd
import os
from updatedb.models import Character, Sword, Claymore, Polearm, Catalyst, Bow, Artifact_set


types = {
    5: 'Sword',
    6: 'Claymore',
    7: 'Polearm',
    8: 'Catalyst',
    9: 'Bow'
}

classess = {
    5: Sword,
    6: Claymore,
    7: Polearm,
    8: Catalyst,
    9: Bow
}


def get_characters():
    df = pd.read_html('https://genshin-impact.fandom.com/wiki/Characters')[2]
    df = df[['Name', 'Weapon', 'Element']]
    df.to_csv('updatedb/scripts/csvs/Character.csv')
    print("Collecting characters - Done")


def get_artifacts():
    df = pd.read_html('https://genshin-impact.fandom.com/wiki/Artifacts/Sets')[1]
    df = df.loc[df['Rarity'] == "4-5★"]
    df[['2 Piece', '4 Piece']] = df.Bonuses.str.split('4 Piece:', expand=True)
    df = df[['Set', '2 Piece', '4 Piece']]
    df['2 Piece'] = df['2 Piece'].str.replace('2 Piece:', '')
    df = df.sort_values(by='Set', ignore_index=True)
    df.to_csv('updatedb/scripts/csvs/Art.csv')
    print("Collecting artifacts - Done")


def get_weapons():
    for weapon_type in range(5, 10):
        df = pd.read_html('https://genshin-impact.fandom.com/wiki/Weapons/List')[weapon_type]
        df = df[['Name', 'Base ATK (Max)', '2nd Stat (Max)', 'Passive Ability']]
        df.to_csv(f'updatedb/scripts/csvs/{types[weapon_type]}.csv')
        print(f'{types[weapon_type]} Done')
    print('Collecting weapons - Done')


def characters():
    file = open('updatedb/scripts/csvs/character.csv')
    read_file = csv.reader(file)

    Character.objects.all().delete()

    count = 1

    for character in read_file:
        if count == 1:
            pass
        else:
            print(character)
            print("-"*90)
            Character.objects.create(name=character[1], weapon=character[2], vision=character[3])
        count += 1


def weapons():
    for weapon_type in range(5, 10):
        file = open(f'updatedb/scripts/csvs/{types[weapon_type]}.csv')
        read_file = csv.reader(file)

        classess[weapon_type].objects.all().delete()

        count = 1

        for item in read_file:
            if count == 1:
                pass
            else:
                print(item)
                print("-" * 90)
                print("\n")
                classess[weapon_type].objects.create(name=item[1], atk=item[2], stat=item[3], ability=item[4])
            count += 1


def artifacts():
    file = open('updatedb/scripts/csvs/Art.csv')
    read_file = csv.reader(file)

    Artifact_set.objects.all().delete()

    count = 1

    for item in read_file:
        if count == 1:
            pass
        else:
            print(item)
            print("-"*90)
            print("\n")
            Artifact_set.objects.create(name=item[1], piece_2=item[2], piece_4=item[3])
        count += 1


def make_csv():
    get_characters()
    get_artifacts()
    get_weapons()
    print('Created csv files')


def run():
    make_csv()
    characters()
    weapons()
    artifacts()


