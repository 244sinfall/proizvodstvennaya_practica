"""App init"""
import argparse
from contracts.composer import VoteDataComposer
from contracts.database import VoteDatabase
from contracts.vote_alg import VoteAlg
from contracts.vote_arranger import DefaultVoteArranger

from composers.version_composer import VersionComposer
from databases.sqlite import SqliteVoteDatabase
from vote_algs.fuzzy_relative_weight_vote_alg import FuzzyRelativeWeightVoteAlg
from vote_arrangers.version_vote_arranger import VersionVoteArranger


class App:
    """Dependency management and runner"""
    def __init__(self,
                 database: VoteDatabase,
                 composer: VoteDataComposer,
                 alg: VoteAlg,
                 arranger: DefaultVoteArranger = DefaultVoteArranger()) -> None:
        self.database = database
        self.composer = composer
        self.alg = alg
        self.arranger = arranger

    def run(self):
        """Runs alg and prints winner"""
        raw = self.database.get_data()
        print(f'Winner selected based on {self.alg.__class__.__name__} algorithm')
        data = [self.composer.compose(entity) for entity in raw]
        self.arranger.arrange(self.alg, data)


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
        database=SqliteVoteDatabase(args.path, args.query),
        composer=VersionComposer(),
        alg=FuzzyRelativeWeightVoteAlg(),
        arranger=VersionVoteArranger()
    )
    app.run()
