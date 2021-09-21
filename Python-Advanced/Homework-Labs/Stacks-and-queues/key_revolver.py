from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
i_value = int(input())
bullets_shot = 0

# load first barrel
barrel = deque()
for n in range(gun_barrel_size):
    if not bullets:
        break
    bullet = bullets.pop()
    barrel.append(bullet)

while True:
    # check if the fired bullet breaks the lock
    current_bullet = barrel.popleft()
    current_lock = locks.popleft()
    if current_bullet <= current_lock:
        print("Bang!")
        bullets_shot += 1
    else:
        print("Ping!")
        bullets_shot += 1
        locks.appendleft(current_lock)
    # reload barrel if Sam is not out of bullets
    if not barrel:
        if not bullets:
            if locks:
                print(f"Couldn't get through. Locks left: {len(locks)}")
                break
        else:
            print("Reloading!")
            for n in range(gun_barrel_size):
                if not bullets:
                    break
                bullet = bullets.pop()
                barrel.append(bullet)
    # check if the safe is cracked
    if not locks:
        print(f"{len(bullets)+len(barrel)} bullets left. Earned ${i_value - bullets_shot*bullet_price}")
        break