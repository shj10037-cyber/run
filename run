import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="🏃‍♂️ 2D 러닝 게임", layout="centered")

st.title("🏃‍♂️ 2D 무한 러닝 게임")
st.caption("스페이스바(Space) 또는 위쪽 화살표(↑)를 눌러 점프하세요!")

# HTML5 Canvas + JavaScript 기반 러닝 게임
game_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        canvas {
            background: linear-gradient(to bottom, #1e1b4b, #312e81);
            display: block;
            margin: 0 auto;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.5);
        }
        body {
            text-align: center;
            font-family: Arial, sans-serif;
            color: white;
            background-color: transparent;
            margin: 0;
            overflow: hidden;
        }
    </style>
</head>
<body>
    <canvas id="gameCanvas" width="600" height="400"></canvas>
    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");

        // 게임 변수
        let score = 0;
        let gameOver = false;
        let gameSpeed = 6;
        let frameCount = 0;

        // 지면 위치
        const groundY = 320;

        // 플레이어 (러너)
        const runner = {
            x: 80,
            y: groundY - 40,
            width: 30,
            height: 40,
            vy: 0,
            gravity: 0.8,
            jumpPower: -13,
            isGrounded: true,
            maxJumps: 2, // 2단 점프 가능
            jumpCount: 0
        };

        // 장애물 배열
        const obstacles = [];

        // 키보드 점프 처리
        document.addEventListener("keydown", (e) => {
            if ((e.key === " " || e.key === "ArrowUp") && !gameOver) {
                if (runner.jumpCount < runner.maxJumps) {
                    runner.vy = runner.jumpPower;
                    runner.isGrounded = false;
                    runner.jumpCount++;
                }
            }
            if (gameOver && (e.key === " " || e.key === "Enter")) {
                resetGame();
            }
        });

        function createObstacle() {
            // 랜덤 장애물 높이/유형 (가시 / 공중 장애물)
            const isFlying = Math.random() < 0.3;
            const height = isFlying ? 30 : Math.random() * 25 + 25;
            const width = Math.random() * 15 + 20;
            const yPos = isFlying ? groundY - 70 : groundY - height;

            obstacles.push({
                x: canvas.width,
                y: yPos,
                width: width,
                height: height,
                color: isFlying ? "#F59E0B" : "#EF4444"
            });
        }

        function resetGame() {
            score = 0;
            gameSpeed = 6;
            frameCount = 0;
            obstacles.length = 0;
            runner.y = groundY - runner.height;
            runner.vy = 0;
            runner.isGrounded = true;
            runner.jumpCount = 0;
            gameOver = false;
            animate();
        }

        function update() {
            if (gameOver) return;

            frameCount++;
            score += 1;

            // 속도 점점 증가
            if (frameCount % 300 === 0) {
                gameSpeed += 0.5;
            }

            // 중력 및 이동 처리
            runner.vy += runner.gravity;
            runner.y += runner.vy;

            // 바닥 착지 처리
            if (runner.y + runner.height >= groundY) {
                runner.y = groundY - runner.height;
                runner.vy = 0;
                runner.isGrounded = true;
                runner.jumpCount = 0;
            }

            // 장애물 생성 (간격 랜덤)
            if (frameCount % Math.max(40, Math.floor(100 - gameSpeed * 3)) === 0) {
                createObstacle();
            }

            // 장애물 이동 및 충돌 체크
            for (let i = 0; i < obstacles.length; i++) {
                let obs = obstacles[i];
                obs.x -= gameSpeed;

                // 충돌 검사 (Hitbox)
                if (
                    runner.x < obs.x + obs.width &&
                    runner.x + runner.width > obs.x &&
                    runner.y < obs.y + obs.height &&
                    runner.y + runner.height > obs.y
                ) {
                    gameOver = true;
                }

                // 화면 밖으로 지나간 장애물 제거
                if (obs.x + obs.width < 0) {
                    obstacles.splice(i, 1);
                    i--;
                }
            }
        }

        function draw() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // 바닥 그리기
            ctx.fillStyle = "#10B981";
            ctx.fillRect(0, groundY, canvas.width, canvas.height - groundY);

            // 플레이어 그리기 (형광 하늘색)
            ctx.fillStyle = "#38BDF8";
            ctx.fillRect(runner.x, runner.y, runner.width, runner.height);

            # 눈 디테일
            ctx.fillStyle = "#FFFFFF";
            ctx.fillRect(runner.x + 18, runner.y + 8, 8, 8);

            // 장애물 그리기
            for (let obs of obstacles) {
                ctx.fillStyle = obs.color;
                ctx.fillRect(obs.x, obs.y, obs.width, obs.height);
            }

            // 점수 및 속도 표시
            ctx.fillStyle = "#FFFFFF";
            ctx.font = "bold 18px Arial";
            ctx.fillText("SCORE: " + Math.floor(score / 5) + " m", 20, 35);
            ctx.font = "14px Arial";
            ctx.fillText("SPEED: " + gameSpeed.toFixed(1) + "x", 20, 60);

            // 게임오버 화면
            if (gameOver) {
                ctx.fillStyle = "rgba(0, 0, 0, 0.75)";
                ctx.fillRect(0, 0, canvas.width, canvas.height);

                ctx.fillStyle = "#FF4D4D";
                ctx.font = "bold 36px Arial";
                ctx.textAlign = "center";
                ctx.fillText("GAME OVER", canvas.width / 2, canvas.height / 2 - 20);

                ctx.fillStyle = "#FFFFFF";
                ctx.font = "18px Arial";
                ctx.fillText("기록: " + Math.floor(score / 5) + " m", canvas.width / 2, canvas.height / 2 + 20);
                ctx.fillText("스페이스바(Space)를 눌러 재도전", canvas.width / 2, canvas.height / 2 + 60);
                ctx.textAlign = "start";
            }
        }

        function animate() {
            update();
            draw();
            if (!gameOver) {
                requestAnimationFrame(animate);
            }
        }

        animate();
    </script>
</body>
</html>
"""

components.html(game_code, height=420)
