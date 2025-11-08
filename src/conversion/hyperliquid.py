
    def __init__(self, full_result, optimizer_run_data):
        self.full_result = full_result
        self.optimizer_run_data = optimizer_run_data
        self.values = {}
        self.score = 0
        self.total_weight = 0

    def compute_score(self, relevant_scoring_parameters):
        self.score = 0
        try:
            self.score = sum([
                self._compute_score(scoring_parameter)
                for scoring_parameter in relevant_scoring_parameters
            ]) / self.total_weight
        except ZeroDivisionError:
            self.score = 0

    def _compute_score(self, fitness_parameter):
        try:
            self.values[fitness_parameter.name] = self.full_result[fitness_parameter.name]
            score = fitness_parameter.get_normalized_value(self.values[fitness_parameter.name])
            self.total_weight += fitness_parameter.weight
            return score
        except KeyError:
            return 0

    def __repr__(self):
        return f"[{self.__class__.__name__}] score: {self.score}, total_weight: {self.total_weight}"

    def result_str(self):
        # todo move constants outside of StrategyDesignOptimizer
        import octobot.strategy_optimizer.strategy_design_optimizer as strategy_design_optimizer
        user_inputs = {
            ui[strategy_design_optimizer.StrategyDesignOptimizer.CONFIG_USER_INPUT]:
                ui[strategy_design_optimizer.StrategyDesignOptimizer.CONFIG_VALUE]
            for ui in self.optimizer_run_data
        }
        return f"fitness score: {self.score} {self.values} from {user_inputs}"
