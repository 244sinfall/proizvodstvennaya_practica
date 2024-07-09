"""App init"""
import argparse
from contracts.composer import VoteDataComposer
from contracts.database import VoteDatabase
from contracts.vote_alg import VoteAlg

from composers.version_composer import VersionComposer
from databases.sqlite import SqliteVoteDatabase
from vote_algs.fuzzy_relative_vote_alg import FuzzyRelativeVoteAlg
from exceptions.vote_exception import VoteException


class App:
    """Dependency management and runner"""
    def __init__(self,
                 database: VoteDatabase,
                 composer: VoteDataComposer,
                 alg: VoteAlg) -> None:
        self.database = database
        self.composer = composer
        self.alg = alg

    def run(self):
        """Runs alg and prints winner"""
        raw = self.database.get_data()
        data = [self.composer.compose(entity) for entity in raw]
        try:
            winner = self.alg.run_vote(data)
            print(f'Winner selected based on {self.alg.__class__.__name__} algorithm: {winner}')
        except VoteException as e:
            print(e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='Vote Runner',
                    description='Runs votes',
                    epilog='done by Dmitry Filin')
    parser.add_argument('-q', '--query',
                        action='store',
                        help='Query to get all experiment data',
                        dest='query',
                        required=True)
    parser.add_argument('-p', '--path',
                        action='store',
                        help='Destination to .db file with experiment data',
                        dest='path',
                          required=True)
    args = parser.parse_args()
    app = App(
        SqliteVoteDatabase(args.path, args.query),
        VersionComposer(),
        FuzzyRelativeVoteAlg()
    )
    app.run()
