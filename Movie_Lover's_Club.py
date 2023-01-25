# Project #3 - Movie Lover's Club
# Student: Rene Tejon
# Student ID: rt891
# Course CRN and Section: 31344 - L01
# Course: MSIT 501 - Foundations of Programming, Data Structures, and Algorithms
# Professor: Dr. Frank J Mitropoulos Ph.D.
# Due Date: February 20, 2022


class MovieClub:
    def __init__(self):
        self.club_data = {
            'Mary': {'Big': {'Watched': 1, 'Rating': 'G'},
                     'Superman': {'Watched': 3, 'Rating': 'PG'},
                     'Forrest Gump': {'Watched': 3, 'Rating': 'PG-13'}
                     },

            'Frank': {'Beauty And The Beast': {'Rating': 'G', 'Watched': 1},
                      'Kung Fu Panda': {'Rating': 'G', 'Watched': 5},
                      'Cinderella': {'Rating': 'G', 'Watched': 1}
                      }
        }
        self.rating = ['G', 'PG', 'PG-13', 'R', 'NC-17', 'UNRATED']

    def menu(self):
        input('\nPress Enter to return to the main menu.')

    def member_list(self):
        print('\n' + '=' * 80)
        print(f"{'Club Members': ^80}")
        print('=' * 80)
        [print(key) for key in self.club_data.keys()]
        self.menu()

    def member_data(self):
        while True:
            print('\n' + '=' * 80)
            print(f"{'Club Member Data ': ^80}")
            print('=' * 80)
            choice = input(
                "1) Single member data"
                "\n2) All member's data"
                "\nQ) Quit to menu"
                "\n\nPlease enter a selection: "
            ).lower().strip()

            if choice == '1':
                name = self.member_check()
                if name == 'q':
                    return
                print('\n' + '=' * 80)
                print(f"{'Movies for club member: ' + name: ^80}")
                print('=' * 80)
                print(f"{'Movie': <50}{'Rating': <15}{'Watched': <15}")
                print('-' * 80)
                member = self.club_data[name]
                for movie in member:
                    movie_rating = self.club_data[name][movie]['Rating']
                    times_watched = self.club_data[name][movie]['Watched']
                    print(f"{movie: <50}{movie_rating: <15}{times_watched: <15}")
                input('\nPress Enter to go back.')
            elif choice == '2':
                all_members = {key for key in self.club_data.keys()}
                for member in all_members:
                    print('\n' + '=' * 80)
                    print(f"{'Movies for club member: ' + member: ^80}")
                    print('=' * 80)
                    print(f"{'Movie': <50}{'Rating': <15}{'Watched': <15}")
                    print('-' * 80)
                    for movie in self.club_data[member]:
                        movie_rating = self.club_data[member][movie]['Rating']
                        times_watched = self.club_data[member][movie]['Watched']
                        print(f"{movie: <50}{movie_rating: <15}{times_watched: <15}")
                input('\nPress Enter to go back.')
            elif choice == 'q':
                break
            else:
                print('\nInvalid input.')

    def member_check(self):
        while True:
            name = input('\nEnter member name or \"Q\" for the main menu: ').title().strip()
            if name in self.club_data.keys():
                return name
            elif name.lower() == 'q':
                return name.lower()
            else:
                print('\nSorry, member not found.')

    def confirm_delete(self, name):
        while True:
            confirm_delete = input('\nAre you sure you want to DELETE \"'
                                   + name
                                   + '\"? Press \"Y\" for yes and \"N\" for no: ').lower().strip()
            if confirm_delete == 'y':
                return confirm_delete
            elif confirm_delete == 'n':
                return confirm_delete
            else:
                print('\nInvalid input.')

    def enter_another_movie(self):
        while True:
            choice = input('\nEnter another movie? Press \"Y\" for yes and \"N\" for no: ').lower().strip()
            if choice == 'y':
                return
            elif choice == 'n':
                return choice
            else:
                print('\nInvalid input.')

    def increment_movie_watched(self):
        print('\n' + '=' * 80)
        print(f"{'Movie Count for Club Members': ^80}")
        print('=' * 80, end='')
        name = self.member_check()
        if name == 'q':
            return

        while name in self.club_data.keys():
            movie_name = input('\nEnter the movie name watched or \"Q\" for the main menu: ').title().strip()
            if movie_name in self.club_data[name]:
                self.club_data[name][movie_name]['Watched'] += 1
                movie_count = self.club_data[name][movie_name]['Watched']
                print('\nMovie count updated.')
                print('=' * 100)
                print(movie_name, '| Watch count:', movie_count - 1, 'Old Value')
                print(movie_name, '| Watch count:', movie_count, 'New Value')
                print('=' * 100)
                another_movie = self.enter_another_movie()
                if another_movie == 'n':
                    return
            elif movie_name.lower() == 'q':
                break
            else:
                print("\nSorry that movie is not in", name + "'s", "record.")

    def add_movie(self):
        print('\n' + '=' * 80)
        print(f"{'Add Movie for Club Members': ^80}")
        print('=' * 80, end='')
        name = self.member_check()
        if name == 'q':
            return

        while True:

            while True:
                new_movie = input('\nEnter name of new movie or \"Q\" for the main menu: ').title().strip()
                if new_movie in self.club_data[name]:
                    print("\nSorry that movie already exists in", name, "'s records")
                elif new_movie.lower() == 'q':
                    return
                else:
                    break

            while True:
                rating = input(
                    '\n' + '*' + '-' * 49 + '*'
                                            '\n  Rating Options: G, PG, PG-13, R, NC-17, Unrated  '
                                            '\n' + '*' + '-' * 49 + '*'
                                                                    '\nEnter rating of movie: '
                ).upper().strip()
                if rating in self.rating:
                    break
                else:
                    print('\nThat is not a valid input.')

            while True:
                try:
                    times_watched = int(input('\nEnter times watched: '))
                    break
                except (ValueError, NameError, SyntaxError, ZeroDivisionError):
                    print('\nThat is not a valid input.')

            self.club_data[name].update({new_movie: {'Rating': rating, 'Watched': times_watched}})
            print('\nDatabase updated.')
            another_movie = self.enter_another_movie()
            if another_movie == 'n':
                return

    def remove_movie(self):
        print('\n' + '=' * 80)
        print(f"{'Club Member Movie Removal': ^80}")
        print('=' * 80, end='')

        name = self.member_check()
        if name == 'q':
            return

        while True:
            remove_movie = input(
                '\nEnter the movie you wish to remove from '
                + name
                + ' or press \"Q\" for the main menu: '
            ).title().strip()
            if remove_movie in self.club_data[name]:
                confirm = self.confirm_delete(remove_movie)
                if confirm == 'y':
                    del self.club_data[name][remove_movie]
                    print('\n' + remove_movie + ' has been removed.')
                    another_movie = self.enter_another_movie()
                    if another_movie == 'n':
                        return
            elif remove_movie.lower() == 'q':
                return
            else:
                print("\nSorry that movie is not in", name + "'s record.")

    def add_member(self):
        print('\n' + '=' * 80)
        print(f"{'Club Member Registration': ^80}")
        print('=' * 80, end='')

        while True:
            new_member = input("\nEnter the new member's name or \"Q\" for the main menu: ").title().strip()
            if new_member in self.club_data.keys():
                print('\nMember already exists.')
            elif new_member.lower() == 'q':
                return
            else:
                break

        self.club_data.update({new_member: {}})
        input(
            '\nMember added. New club member registration complete. '
            '\n\nPress Enter to return to main menu.'
        )

    def remove_member(self):
        print('\n' + '=' * 80)
        print(f"{'Club Member Movie Removal': ^80}")
        print('=' * 80, end='')

        name = self.member_check()
        if name == 'q':
            return

        confirm = self.confirm_delete(name)
        if confirm == 'y':
            del self.club_data[name]
            print('\nMember data for', name, 'has been deleted.')
        self.menu()


def main():
    m = MovieClub()
    menu = ''

    while menu != 'q':
        menu = input(
            "\n*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*"
            "\n  Welcome to the Movie Lover's Club "
            "\n*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*"
            "\n1. Display all members"
            "\n2. Display all movie information for members"
            "\n3. Increment the times a specific movie was watched by a member"
            "\n4. Add a new movie for a member"
            "\n5. Remove a movie from member data"
            "\n6. Add a new member"
            "\n7. Remove a member"
            "\nQ. Quit"
            "\n\nPlease enter a selection: "
        ).lower().strip()
        if menu == '1':
            m.member_list()
        elif menu == '2':
            m.member_data()
        elif menu == '3':
            m.increment_movie_watched()
        elif menu == '4':
            m.add_movie()
        elif menu == '5':
            m.remove_movie()
        elif menu == '6':
            m.add_member()
        elif menu == '7':
            m.remove_member()
        elif menu == 'q':
            print("\nThanks for using the Movie Lover's Club application!")
            quit()
        else:
            print('\nInvalid input.')


if __name__ == '__main__':
    main()
