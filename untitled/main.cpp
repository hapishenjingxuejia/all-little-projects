#include <SFML/Graphics.hpp>
#include <random>

int main()
{
    sf::RenderWindow window(sf::VideoMode(800, 600), "Fireworks Animation");

    std::random_device rd;
    std::default_random_engine generator(rd());
    std::uniform_real_distribution<float> distribution(-4.0f, 4.0f);

    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        window.clear();

        // 随机生成烟花的位置和颜色
        float x = 400.0f + distribution(generator) * 100.0f;
        float y = 500.0f + distribution(generator) * 100.0f;
        sf::Color color(distribution(generator) * 255.0f, distribution(generator) * 255.0f, distribution(generator) * 255.0f);

        for (int i = 0; i < 100; i++)
        {
            // 随机生成烟花爆炸的速度和方向
            float vx = distribution(generator) * 2.0f;
            float vy = distribution(generator) * 2.0f;

            sf::CircleShape particle(4.0f);
            particle.setPosition(x, y);
            particle.setFillColor(color);

            while (particle.getPosition().y > 0)
            {
                particle.move(vx, vy);
                vy += 0.1f;

                window.draw(particle);
                window.display();
            }
        }

        window.display();
    }

    return 0;
}
