class Solution:
    def winner(self, contest_scores, num_contestants):
        score_frequency = {}
        max_frequency, result_scores = 0, []

        for score in contest_scores:
            score_frequency[score] = score_frequency.get(score, 0) + 1
            max_frequency = max(max_frequency, score_frequency[score])

        for score, frequency in score_frequency.items():
            if frequency == max_frequency:
                result_scores.append(score)

        result_scores.sort()
        return result_scores[0], max_frequency
