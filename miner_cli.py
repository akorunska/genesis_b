import cmd
from pitcoin_modules.blockchain import Blockchain


class MinerCLI(cmd.Cmd):
    intro = 'Welcome to pitcoin_modules miner-cli. Type help or ? to list commands.\n'
    prompt = '\n(pitcoin-miner-cli) '
    blockchain = Blockchain()
    i = 0

    def do_mine(self, arg):
        while True:
            result = self.blockchain.mine_and_submit_block()
            if result:
                print("new block was mined and broadcast to the network. block hash is: ", result)
            else:
                print("block was mined by other node, continuing on the new chain.")

    def do_quit(self, arg):
        'Exit wallet-cli shell'
        print('Thank you for using pitcoin-miner-cli')
        return True


if __name__ == '__main__':
    MinerCLI().cmdloop()


