# Write your MySQL query statement below
# Leetcode : https://leetcode.com/problems/rank-scores/
SELECT Score AS score,
       @rank:=(SELECT COUNT(DISTINCT(S1.Score))+1 FROM Scores AS S1 WHERE S1.Score > S.Score)          AS  'Rank'
       FROM Scores AS S
       ORDER BY S.Score DESC;