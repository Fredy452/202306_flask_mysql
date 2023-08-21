select * from users;

INSERT INTO users(first_name, last_name) VALUES("Ilins", "wfbw");
INSERT INTO users(first_name, last_name) VALUES("Maria", "Huay");
INSERT INTO users(first_name, last_name) VALUES("Jose", "Poau");
INSERT INTO users(first_name, last_name) VALUES("Ma", "IOTRE");

#Making friends
INSERT INTO friendships(user_id, friend_id) VALUES(3, 2);
INSERT INTO friendships(user_id, friend_id) VALUES(4, 1);
# Showing friends
SELECT concat(users.first_name,' ', users.last_name) AS User, concat(user2.first_name,' ',user2.last_name) AS Friend
FROM users
JOIN friendships ON users.id = friendships.user_id
JOIN users AS user2 ON user2.id = friendships.friend_id;