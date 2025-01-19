import pandas as pd
import sqlite3
from models import Veiculos


# desc_detalhada = {
#    "Corolla": "O Toyota Corolla é um dos sedãs compactos mais populares e confiáveis do mundo. Conhecido por sua eficiência, conforto e acessibilidade, o Corolla apresenta um design elegante, excelente economia de combustível e uma reputação de longevidade. Possui tecnologias de segurança avançadas como o Toyota Safety Sense, tornando-o uma escolha ideal para trajetos diários e famílias.",
    
#     "Civic": "O Honda Civic combina design esportivo com praticidade. Oferece uma variedade de versões, incluindo opções de sedã, cupê e hatchback. Com sua linha de motores eficientes, manuseio ágil e interior tecnológico, o Civic é perfeito para motoristas que buscam equilíbrio entre desempenho e economia. O Civic também inclui o pacote de segurança Honda Sensing como padrão em muitos modelos.",
    
#     "Mustang": "O Ford Mustang é um carro esportivo icônico americano. Conhecido por seu estilo arrojado, opções de motores V8 potentes e desempenho emocionante, o Mustang oferece uma experiência de direção empolgante. Seja em um cupê clássico ou um GT de alto desempenho, o Mustang oferece algo para todos os entusiastas de desempenho.",
    
#     "Camaro": "O Chevrolet Camaro é um competidor feroz na categoria de carros esportivos. Com design agressivo, uma variedade de motores potentes e manuseio excelente, o Camaro foi projetado para oferecer desempenho emocionante. Está disponível nas versões cupê e conversível, com opções como o ZL1 para aqueles que buscam potência extrema.",
    
#     "X5": "O BMW X5 é um SUV de luxo médio que combina desempenho refinado com tecnologia avançada. Oferecendo uma gama de motores, de seis cilindros turbo a V8 potentes, o X5 proporciona uma condução suave, manuseio excepcional e um interior premium. Está equipado com tecnologias e recursos de segurança de ponta, tornando-o um dos principais concorrentes no segmento de SUVs de luxo.",
    
#     "C-Class": "O Mercedes-Benz Classe C é um sedã compacto de luxo que oferece uma combinação de sofisticação, desempenho e conforto. Seu interior de alta qualidade, condução suave e opções de motores potentes, incluindo híbridos, tornam-no uma escolha atraente para quem procura uma experiência de direção luxuosa. Recursos avançados de segurança e um sistema de infotainment fácil de usar aumentam seu apelo.",
    
#     "A4": "O Audi A4 é um sedã compacto de luxo que oferece um equilíbrio refinado de desempenho, tecnologia e conforto. Com o sistema Quattro de tração integral, motor turbo suave e interior premium, o A4 é uma escolha ideal para quem procura um carro elegante e ágil. Ele também possui recursos avançados de segurança e infotainment intuitivo.",
    
#     "Altima": "O Nissan Altima é um sedã médio que se destaca pelo design elegante, opções de motor eficientes e condução confortável. Com tração integral disponível, oferece melhor aderência em diversas condições climáticas. Também vem com o Nissan ProPilot Assist, um conjunto de recursos de assistência ao motorista, tornando-o uma opção segura e confiável para famílias.",
    
#     "CX-5": "O Mazda CX-5 é um crossover compacto que combina manuseio esportivo com um interior premium. Seu design exterior elegante, opções de motor responsivas e cabine sofisticada fazem dele um destaque em seu segmento. Com uma série de recursos de segurança padrão e uma reputação de confiabilidade, o CX-5 é ideal para motoristas que buscam um SUV funcional e divertido.",
    
#     "Outback": "O Subaru Outback é um crossover versátil e robusto projetado para entusiastas de aventuras ao ar livre. Com tração integral padrão e excelente altura do solo, o Outback está pronto para aventuras dentro e fora da estrada. Seu interior espaçoso, sistema de infotainment fácil de usar e fortes recursos de segurança o tornam um excelente veículo para famílias.",
    
#     "Elantra": "O Hyundai Elantra é um sedã compacto que oferece design moderno, interior espaçoso e uma série de recursos tecnológicos. Conhecido por sua eficiência e acessibilidade, o Elantra possui uma gama de motorização, incluindo opções híbridas. Ele também conta com uma garantia impressionante e recursos avançados de segurança.",
    
#     "Soul": "O Kia Soul é um hatchback compacto com um design distinto que se destaca em ambientes urbanos. Oferecendo uma cabine espaçosa, tecnologia intuitiva e preço acessível, o Soul é um carro divertido e funcional. Ele vem com uma variedade de motores e oferece uma condução suave e confortável com amplo espaço para bagagem.",
    
#     "Wrangler": "O Jeep Wrangler é o SUV off-road definitivo, conhecido por seu design robusto e capacidades incomparáveis fora da estrada. Com portas e teto removíveis, oferece uma experiência de direção ao ar livre única. Seu sistema 4x4 e motores robustos o tornam o veículo preferido para aventureiros que buscam emoção dentro e fora das trilhas.",
    
#     "Discovery": "O Land Rover Discovery é um SUV de luxo que combina capacidade off-road com conforto de alto nível. Ele oferece um sistema avançado de tração integral, um interior luxuoso e espaçoso e alta capacidade de reboque. O Discovery é ideal para quem deseja um veículo capaz de enfrentar terrenos difíceis com sofisticação.",
    
#     "XC90": "O Volvo XC90 é um SUV de luxo médio que oferece um interior premium, recursos avançados de segurança e uma condução suave e equilibrada. Com opções de motorização híbrida, o XC90 combina eficiência e desempenho. Seu espaço para três fileiras de assentos, materiais de alta qualidade e tecnologia de ponta fazem dele um veículo ideal para famílias.",
    
#     "Model 3": "O Tesla Model 3 é um sedã totalmente elétrico que combina tecnologia de ponta, autonomia impressionante e desempenho excepcional. Com aceleração rápida, um sistema de infotainment intuitivo e atualizações de software over-the-air, o Model 3 lidera a inovação em veículos elétricos. Também é conhecido por seu interior minimalista e design elegante.",
    
#     "911": "O Porsche 911 é um carro esportivo de alto desempenho reverenciado por sua engenharia de precisão, design atemporal e experiência de condução emocionante. Disponível em várias configurações, incluindo modelos turbo e conversíveis, o 911 oferece manuseio excepcional, uma linha de motores potentes e um interior luxuoso.",
    
#     "F-Pace": "O Jaguar F-Pace é um SUV de luxo que combina desempenho dinâmico com recursos premium. Ele oferece manuseio preciso, design elegante e uma gama de motores potentes. Com um interior de alta qualidade, assentos espaçosos e ampla capacidade de carga, o F-Pace é um veículo versátil que se destaca em desempenho e praticidade.",
    
#     "Roma": "O Ferrari Roma é um grand tourer de alto desempenho que combina o desempenho icônico da Ferrari com usabilidade diária. Com um potente motor V8, design elegante e interior sofisticado, o Roma é perfeito para quem busca uma condução emocionante com um design refinado. Ele oferece uma combinação incomparável de potência, conforto e requinte.",
    
#     "Huracán": "O Lamborghini Huracán é um supercarro que oferece desempenho incomparável e estética deslumbrante. Com um motor V10 naturalmente aspirado, tração integral e manuseio preciso, o Huracán é construído para velocidade e emoção. Seu design agressivo, interior luxuoso e desempenho eletrizante o tornam um carro dos sonhos para entusiastas.",
    
#     "720S": "O McLaren 720S é um hipercarro que oferece desempenho extremo, tecnologia de ponta e uma estrutura leve de fibra de carbono. Com um motor V8 biturbo de 720 cavalos, o 720S oferece aceleração impressionante e manuseio de primeira linha. Seu design futurista, recursos luxuosos e capacidades para pista o tornam um destaque no mundo dos supercarros.",
    
#     "Panigale V4": "A Ducati Panigale V4 é uma máquina inspirada nas corridas que traz tecnologia MotoGP para as ruas. Com motor V4 de 1.103cc produzindo 214 cavalos, oferece uma experiência de pilotagem emocionante. A Panigale V4 é equipada com eletrônica avançada, incluindo IMU de seis eixos, ABS nas curvas, controle de tração e quickshifter, tornando-a incrivelmente ágil e precisa. Seu design aerodinâmico, manuseio preciso e sistema de suspensão de ponta garantem que esta superbike se destaque tanto na pista quanto na estrada.",
    
#     "Street Glide": "A Harley-Davidson Street Glide é uma cruiser touring que combina o estilo icônico da Harley-Davidson com conforto para longas distâncias. Equipada com motor Milwaukee-Eight 107 V-Twin, oferece uma pilotagem suave e potente. Possui sistema de infotainment Boom!™ Box GTS, assentos confortáveis e alforjes para amplo armazenamento. Com seu perfil baixo e estética personalizada, a Street Glide é perfeita para motociclistas que buscam viajar com conforto e estilo.",
    
#     "R1250GS": "A BMW R1250GS é uma moto aventureira-touring conhecida por sua capacidade off-road e refinamento em estrada. Equipada com motor boxer twin de 1.254cc, produz 136 cavalos e possui sistema de suspensão ESA dinâmico, garantindo estabilidade e conforto em diversos terrenos. Com tecnologias avançadas como modos de pilotagem, ABS nas curvas e controle de tração dinâmico, a R1250GS é projetada para motociclistas que buscam exploração, seja dentro ou fora da estrada.",
    
#     "YZF-R1": "A Yamaha YZF-R1 é uma superbike premium projetada para entusiastas de pista e pilotos de rua. Seu motor de 998cc quatro cilindros em linha, produzindo cerca de 200 cavalos, é inspirado na experiência da Yamaha no MotoGP. A R1 oferece eletrônica avançada como controle de deslizamento, controle de largada e quickshifter, além de um sofisticado sistema de suspensão. Seu estilo agressivo e chassi leve a tornam uma máquina potente e ágil, perfeita para pilotagem de alta performance.",
    
#     "1290 Super Duke R": "A KTM 1290 Super Duke R é uma naked brutal e potente projetada para o máximo desempenho. Equipada com motor V-twin de 1.301cc, entrega 180 cavalos, oferecendo aceleração impressionante e torque de primeira linha. A Super Duke R possui eletrônica avançada como controle de tração, ABS nas curvas e modos de pilotagem, e é equipada com chassi leve e suspensão ajustável para manuseio excepcional. Seu design agressivo e potência bruta a tornam uma das motos mais emocionantes do mercado.",
    
#     "CBR1000RR": "A Honda CBR1000RR, também conhecida como Fireblade, é uma superbike que combina engenharia de precisão com desempenho. Equipada com motor de 999cc quatro cilindros em linha, produz cerca de 189 cavalos, oferecendo excelente desempenho em alta velocidade. A CBR1000RR possui um chassi altamente responsivo, auxílios eletrônicos ao piloto incluindo modos de pilotagem selecionáveis, controle de tração e ABS. É projetada para oferecer agilidade e estabilidade de primeira linha, tornando-a uma escolha principal para pilotos tanto de pista quanto de rua.",
    
#     "Hayabusa": "A Suzuki Hayabusa é uma moto esportiva lendária que estabeleceu o padrão para desempenho em alta velocidade. Com seu motor de 1.340cc quatro cilindros em linha, entrega 188 cavalos e imensa velocidade final, capaz de ultrapassar 290 km/h. Seu design aerodinâmico, junto com suspensão refinada e sistema de freios, proporciona excelente estabilidade em altas velocidades. Conhecida por seu equilíbrio entre potência e conforto, a Hayabusa é perfeita para motociclistas que desejam aceleração incomparável e pilotagem suave.",
    
#     "Street Triple": "A Triumph Street Triple é uma naked dinâmica e ágil que se destaca tanto em deslocamentos urbanos quanto em pilotagem esportiva. Equipada com motor tricilíndrico de 765cc, entrega empolgantes 121 cavalos, com um ronco distinto que adiciona à experiência. A Street Triple é conhecida por seu manuseio leve, oferecendo precisão nas curvas e resposta aguçada. Com auxílios modernos ao piloto, incluindo controle de tração, acelerador eletrônico e múltiplos modos de pilotagem, é uma moto versátil para qualquer motociclista.",
    
#     "Ninja ZX-10R": "A Kawasaki Ninja ZX-10R é uma superbike projetada com DNA de pista e capacidade para rua. Equipada com motor de 998cc quatro cilindros em linha, a ZX-10R produz 200 cavalos, tornando-a uma fera na pista. A moto possui eletrônica de ponta como controle de largada, ABS nas curvas e quickshifter KQS da Kawasaki. Com sua carenagem aerodinâmica, suspensão refinada e sistema de freios superior, a Ninja ZX-10R é construída para velocidade, precisão e desempenho geral na pista.",
    
#     "Vespa GTS 300": "A Vespa GTS 300 é um scooter elegante e moderno que combina elegância italiana com praticidade urbana. Equipada com motor monocilíndrico de 278cc, oferece aceleração suave e ótima eficiência de combustível para deslocamentos urbanos. Com design clássico refinado, amplo espaço de armazenamento sob o assento e recursos como iluminação LED e painel digital, a GTS 300 é uma escolha ideal para motociclistas que buscam conforto e estilo em ambiente urbano.",

#     "RSV4": "A Aprilia RSV4 é uma superbike de alto desempenho conhecida por seu pedigree nas corridas e experiência de pilotagem emocionante. Equipada com motor V4 de 1.099cc, a RSV4 entrega cerca de 217 cavalos, tornando-a uma das principais concorrentes em sua classe. Possui eletrônica avançada, incluindo ABS nas curvas, controle de tração e modos de potência dinâmicos, além de suspensão totalmente ajustável. Com seu estilo agressivo e manuseio preciso, a RSV4 é construída para track days e entusiastas sérios.",

#     "Brutale 1000 RR": "A MV Agusta Brutale 1000 RR é uma moto hyper-naked que combina desempenho extremo com design de ponta. Equipada com motor quatro cilindros em linha de 998cc, entrega cerca de 208 cavalos e torque excepcional. A Brutale 1000 RR é equipada com eletrônica de alto nível, incluindo quickshifter sofisticado, controle de tração e sistema de freios avançado. Com seu design marcante, suspensão avançada e manuseio preciso, é uma moto emocionante para motociclistas que buscam tanto potência quanto estilo.",

#     "Tahoe": "O Chevrolet Tahoe é um SUV grande conhecido por seu interior espaçoso, opções de motores potentes e impressionante capacidade de reboque. Com três fileiras de assentos, recursos tecnológicos avançados e capacidade off-road, o Tahoe é perfeito tanto para famílias grandes quanto para aventureiros.",

#     "1500": "A Ram 1500 é uma picape grande que oferece uma combinação de força, conforto e luxo. Com uma variedade de opções de motor, incluindo um sistema híbrido leve, proporciona excelente capacidade de reboque e qualidade de condução suave. Seu interior sofisticado, tecnologia avançada e capacidade robusta a tornam uma das principais escolhas para entusiastas de picapes.",

#     "F-150": "A Ford F-150 é uma das picapes mais vendidas nos EUA, conhecida por sua versatilidade, durabilidade e desempenho. Com uma variedade de motorizações, incluindo opção híbrida, a F-150 oferece capacidades de carga e reboque líderes da categoria. Seu interior high-tech e design robusto a tornam adequada tanto para trabalho quanto para lazer.",

#     "Tacoma": "A Toyota Tacoma é uma picape média que oferece capacidade off-road, durabilidade e forte reputação de confiabilidade. Com tração 4x4 disponível e design robusto, a Tacoma é perfeita para aventuras ao ar livre e reboque. Também oferece uma cabine confortável e recursos tecnológicos modernos, tornando-a uma excelente picape polivalente.",

#     "Frontier": "A Nissan Frontier é uma picape média que proporciona excelente custo-benefício, desempenho sólido e capacidade off-road. Com design moderno, motores eficientes e interior amigável, a Frontier é uma ótima escolha tanto para uso diário quanto para tarefas relacionadas ao trabalho.",

#     "Land Cruiser": "O Toyota Land Cruiser é um SUV off-road lendário que combina capacidade robusta com recursos luxuosos. Conhecido por sua durabilidade e destreza fora de estrada, o Land Cruiser é projetado para enfrentar os terrenos mais difíceis enquanto proporciona uma experiência de direção confortável e sofisticada.",

#     "Ranger": "A Ford Ranger é uma picape média que oferece impressionante capacidade de reboque e interior high-tech. Com opção de motor turbo, excelente economia de combustível e condução suave, a Ranger é perfeita para quem procura uma picape capaz e prática.",

#     "Chiron": "O Bugatti Chiron é um hipercarro exclusivo que oferece desempenho impressionante e luxo incomparável. Com um motor W16 quad-turbo de 8.0 litros, o Chiron pode atingir velocidades impressionantes, tornando-o um dos carros mais rápidos do mundo. Seu interior opulento e acabamento artesanal o tornam uma verdadeira obra de arte.",

#     "Jesko": "O Koenigsegg Jesko é um hipercarro construído para velocidade e precisão. Com motor V8 biturbo, aerodinâmica avançada e estrutura leve em fibra de carbono, o Jesko foi projetado para empurrar os limites do desempenho. Possui tecnologia de ponta e é um dos principais concorrentes no mundo dos hipercarros.",

#     "Leaf": "O Nissan Leaf é um dos veículos elétricos (EVs) mais acessíveis e práticos do mercado. Com design prático, interior espaçoso e conjunto motriz elétrico eficiente, o Leaf é perfeito para quem busca um carro ecológico com excelente custo-benefício. Seu tamanho compacto e baixos custos operacionais o tornam ideal para direção urbana.",

#     "e": "O Honda e é um veículo elétrico compacto projetado para ambientes urbanos. Com estilo retrô-inspirado, natureza divertida de dirigir e interior repleto de tecnologia, o Honda e traz uma nova visão sobre mobilidade elétrica. Seu tamanho compacto, manuseio ágil e recursos sustentáveis o tornam ideal para vida urbana.",

#     "Cooper SE": "O Mini Cooper SE é a versão totalmente elétrica do icônico Mini Cooper. Mantém o tamanho compacto característico da marca, dirigibilidade tipo kart e design elegante, oferecendo uma experiência de direção totalmente elétrica. Com personalidade divertida e vibrante, o Cooper SE é perfeito para quem procura um carro compacto ecológico com toque premium.",

#     "EQ Fortwo": "O Smart EQ Fortwo é um carro elétrico pequeno projetado para vida urbana. Com suas dimensões compactas, o Fortwo se destaca em espaços apertados e estacionamentos da cidade. Apesar do tamanho, oferece uma condução surpreendentemente confortável e vem com recursos tecnológicos avançados, tornando-o ideal para moradores urbanos conscientes do meio ambiente.",

#     "Silverado": "O Chevrolet Silverado é uma picape grande que combina força robusta com tecnologia avançada. Com opções de motores potentes, cabine espaçosa e impressionante capacidade de reboque, o Silverado é perfeito tanto para trabalho quanto para lazer. Seus recursos versáteis e sistema de infotainment moderno o tornam uma escolha principal para compradores de picapes.",

#     "Accord": "O Honda Accord é um sedã médio que oferece um equilíbrio perfeito entre desempenho, eficiência e conforto. Com interior espaçoso, tecnologia avançada e variedade de opções de motor, incluindo modelos híbridos, o Accord é perfeito para famílias e pessoas que fazem deslocamento diário. É conhecido por sua longevidade e forte valor de revenda.",

#     "Camry": "O Toyota Camry é um sedã médio que combina confiabilidade com design elegante. Com seu interior confortável, motores eficientes e condução suave, o Camry é uma excelente escolha para motoristas diários. Disponível em versões híbrida e a gasolina, também vem com um conjunto de recursos de segurança, incluindo Toyota Safety Sense.",

#     "Sonata": "O Hyundai Sonata é um sedã médio que se destaca com seu design moderno e tecnologia avançada. Com uma variedade de motores, incluindo opção híbrida, o Sonata oferece excelente economia de combustível, condução confortável e diversos recursos padrão, incluindo sistemas avançados de assistência ao motorista.",

#     "Explorer": "O Ford Explorer é um SUV médio com três fileiras de assentos, tornando-o perfeito para famílias. Oferece uma variedade de opções de motor, incluindo híbridos, e entrega excelente capacidade de reboque. Com interior sofisticado, recursos tecnológicos intuitivos e sólida capacidade off-road, o Explorer é uma escolha ideal para famílias aventureiras.",

#     "Equinox": "O Chevrolet Equinox é um SUV compacto que oferece cabine espaçosa, condução confortável e desempenho sólido. Com uma variedade de escolhas de motor e recursos tecnológicos padrão como Apple CarPlay e Android Auto, o Equinox é perfeito para quem procura um veículo versátil e familiar.",

#     "3 Series": "O BMW Série 3 é um sedã compacto de luxo conhecido por sua esportividade e recursos sofisticados. Com manuseio preciso, opções de motores potentes e interior refinado, o Série 3 proporciona uma experiência de direção premium. Seus recursos tecnológicos e de segurança avançados o tornam um dos principais concorrentes no mercado de sedãs de luxo.",

#     "Q5": "O Audi Q5 é um SUV compacto de luxo que combina desempenho refinado com tecnologia de ponta. Com interior confortável e sofisticado, tração integral Quattro padrão e variedade de opções de motor, o Q5 oferece uma experiência de direção suave e dinâmica, tornando-o perfeito tanto para direção urbana quanto para aventuras ao ar livre.",

#     "E-Class": "O Mercedes-Benz Classe E é um sedã de luxo que oferece uma combinação perfeita de desempenho, tecnologia e conforto. Com uma variedade de opções de motor, incluindo variantes híbridas, o Classe E proporciona uma experiência de direção emocionante. Seu interior elegante, recursos avançados de segurança e sistema de infotainment fácil de usar o tornam uma escolha principal para compradores exigentes.",

#     "Model S": "O Tesla Model S é um sedã de luxo totalmente elétrico que oferece desempenho, tecnologia e autonomia de ponta. Com aceleração impressionante, recursos de piloto automático e interior minimalista, o Model S redefine o segmento de sedãs de luxo. Sua bateria de longa autonomia e carregamento rápido o tornam ideal para quem procura uma experiência de direção elétrica premium.",

#     "Murano": "O Nissan Murano é um SUV médio que oferece condução confortável, interior espaçoso e design elegante. Com motor V6 e opções de tração dianteira ou integral, o Murano proporciona uma experiência de direção suave e responsiva. Também vem com sistema de infotainment intuitivo e recursos de segurança padrão, tornando-o uma ótima escolha para famílias.",

#     "XE": "O Jaguar XE é um sedã compacto de luxo que oferece uma experiência de direção refinada e dinâmica. Com manuseio preciso, escolha de motores potentes e interior luxuoso, o XE é uma combinação perfeita de esportividade e conforto. Seu design elegante e recursos tecnológicos avançados o tornam uma escolha ideal para quem busca uma direção elegante e envolvente."
# }

# desc_rapida = {
#     "Corolla": "Confiável, eficiente e acessível. Excelente economia de combustível e recursos avançados de segurança.",
#     "Civic": "Esportivo, eficiente e com tecnologia avançada. Ideal para um equilíbrio entre desempenho e praticidade.",
#     "Mustang": "Ícone do muscle car americano com motor V8 e desempenho emocionante para verdadeiros entusiastas.",
#     "Camaro": "Estilo agressivo e motores poderosos para desempenho de tirar o fôlego.",
#     "X5": "SUV de luxo com desempenho refinado, tecnologia de ponta e manuseio excepcional.",
#     "C-Class": "Sedã compacto de luxo oferecendo sofisticação, desempenho e recursos avançados de segurança.",
#     "A4": "Desempenho refinado e recursos premium com tração integral característica da Audi.",
#     "Altima": "Sedã de porte médio com design elegante, motores eficientes e recursos avançados de assistência ao motorista.",
#     "CX-5": "Manuseio esportivo, interior premium e recursos de segurança de ponta em um SUV compacto.",
#     "Outback": "Crossover robusto e versátil com tração integral e capacidades off-road.",
#     "Elantra": "Sedã compacto com estilo moderno, excelente eficiência e recursos tecnológicos avançados.",
#     "Soul": "Design distinto, interior espaçoso e tecnologia fácil de usar em um hatchback divertido e funcional.",
#     "Wrangler": "Pronto para off-road com portas e teto removíveis para uma experiência de aventura única.",
#     "Discovery": "SUV de luxo combinando destreza off-road com conforto e tecnologia de alto nível.",
#     "XC90": "SUV premium com amplo espaço para três fileiras de assentos, segurança avançada e opções híbridas.",
#     "Model 3": "Sedã totalmente elétrico com desempenho excepcional, tecnologia e design minimalista.",
#     "911": "Esportivo atemporal com manuseio preciso, motores poderosos e interiores luxuosos.",
#     "F-Pace": "SUV de luxo dinâmico oferecendo desempenho, conforto e amplo espaço de carga.",
#     "Roma": "Grand tourer da Ferrari com motor V8, estilo elegante e recursos de luxo.",
#     "Huracán": "Supercarro deslumbrante com motor V10, tração integral e desempenho extraordinário.",
#     "720S": "Hypercar com desempenho extremo, design leve e tecnologia de ponta.",
#     "Panigale V4": "Superbike inspirada nas corridas com tecnologia MotoGP, oferecendo desempenho emocionante.",
#     "Street Glide": "Cruiser de turismo com estilo icônico da Harley-Davidson e conforto para longas distâncias.",
#     "R1250GS": "Motocicleta de aventura e turismo com destreza off-road, conforto e tecnologia avançada.",
#     "YZF-R1": "Superbike inspirada na MotoGP com desempenho poderoso e manuseio preciso.",
#     "1290 Super Duke R": "Naked bike potente com aceleração impressionante e manuseio de primeira linha.",
#     "CBR1000RR": "Superbike com engenharia precisa, agilidade excepcional e potência de alto desempenho.",
#     "Hayabusa": "Esportiva lendária oferecendo aceleração incomparável e velocidade final.",
#     "Street Triple": "Naked bike ágil com manuseio afiado e desempenho dinâmico para cidade e pista.",
#     "Ninja ZX-10R": "Superbike de origem nas corridas com potência extrema, manuseio preciso e eletrônica avançada.",
#     "Vespa GTS 300": "Scooter estilosa e prática, oferecendo uma condução suave pela cidade com um toque italiano.",
#     "RSV4": "Superbike de alto desempenho com pedigree de corrida e manuseio emocionante.",
#     "Brutale 1000 RR": "Naked bike hipernova com desempenho extremo, design de ponta e manuseio preciso.",
#     "Tahoe": "SUV de porte grande com assentos espaçosos, motores potentes e capacidades off-road.",
#     "1500": "Pickup de porte grande oferecendo força, luxo e excelente capacidade de reboque.",
#     "F-150": "Camionete mais vendida com desempenho versátil, durabilidade e recursos tecnológicos.",
#     "Tacoma": "Pickup de porte médio com design robusto, capacidade off-road e confiabilidade.",
#     "Frontier": "Camionete de porte médio com desempenho sólido, design moderno e prontidão para off-road.",
#     "Land Cruiser": "SUV lendário off-road com durabilidade, luxo e conforto para terrenos difíceis.",
#     "Ranger": "Camionete de porte médio oferecendo impressionante capacidade de reboque, eficiência de combustível e recursos de alta tecnologia.",
#     "Chiron": "Hypercar exclusivo com velocidade impressionante, luxo inigualável e acabamento sob medida.",
#     "Jesko": "Hypercar construído para desempenho extremo com aerodinâmica e tecnologia de ponta.",
#     "Leaf": "Veículo elétrico acessível e prático, com tamanho compacto e excelente autonomia para a cidade.",
#     "e": "Veículo elétrico compacto com estilo retrô, manuseio ágil e interior cheio de tecnologia.",
#     "Cooper SE": "Mini totalmente elétrico com manuseio divertido, tamanho compacto e recursos premium.",
#     "EQ Fortwo": "Pequeno carro urbano totalmente elétrico com manuseio ágil e recursos ecológicos.",
#     "Silverado": "Camionete de porte grande oferecendo força robusta, poder de reboque e recursos tecnológicos avançados.",
#     "Accord": "Sedã de porte médio oferecendo a combinação perfeita de desempenho, eficiência e conforto.",
#     "Camry": "Sedã confiável de porte médio com motores eficientes, condução suave e recursos avançados de segurança.",
#     "Sonata": "Sedã moderno de porte médio com design elegante, excelente economia de combustível e tecnologia avançada.",
#     "Explorer": "SUV de porte médio com três fileiras de assentos, capacidades off-road e opções híbridas.",
#     "Equinox": "SUV compacto oferecendo uma condução confortável, recursos tecnológicos e excelente economia de combustível.",
#     "3 Series": "Sedã de luxo conhecido por seu esportividade, manuseio preciso e recursos sofisticados.",
#     "Q5": "SUV compacto de luxo com desempenho refinado, tração integral e tecnologia avançada.",
#     "E-Class": "Sedã de luxo oferecendo desempenho, tecnologia e uma experiência de condução refinada.",
#     "Model S": "Sedã de luxo totalmente elétrico com desempenho excepcional, autonomia e tecnologia de ponta.",
#     "Murano": "SUV de porte médio estiloso com condução confortável, motor V6 e recursos tecnológicos intuitivos.",
#     "XE": "Sedã compacto de luxo oferecendo desempenho refinado, manuseio preciso e um interior premium."
# }

# data_de_revisao = {'Corolla': '2024-07-02', 'Civic': '2025-06-10', 'Mustang': '2024-11-28', 'Camaro': '2024-05-24', 'X5': '2024-09-19', 'C-Class': '2025-10-17', 'A4': '2025-09-29', 'Altima': '2025-05-03', 'CX-5': '2025-07-28', 'Outback': '2025-10-31', 'Elantra': '2025-12-05', 'Soul': '2025-11-09', 'Wrangler': '2025-11-30', 'Discovery': '2024-06-29', 'XC90': '2025-12-17', 'Model 3': '2025-06-03', '911': '2025-08-14', 'F-Pace': '2026-01-03', 'Roma': '2025-05-31', 'Huracán': '2025-12-09', '720S': '2025-04-14', 'Panigale V4': '2025-02-05', 'Street Glide': '2025-01-07', 'R1250GS': '2024-11-30', 'YZF-R1': '2025-07-12', '1290 Super Duke R': '2024-05-05', 'CBR1000RR': '2024-09-21', 'Hayabusa': '2024-03-15', 'Street Triple': '2025-11-19', 'Ninja ZX-10R': '2024-08-22', 'Vespa GTS 300': '2025-06-17', 'RSV4': '2025-05-11', 'Brutale 1000 RR': '2025-07-18', 'Tahoe': '2025-04-13', '1500': '2025-04-06', 'F-150': '2025-06-18', 'Tacoma': '2025-08-31', 'Frontier': '2024-04-09', 'Land Cruiser': '2025-01-04', 'Ranger': '2024-10-19', 'Chiron': '2024-11-30', 'Jesko': '2024-06-01', 'Leaf': '2025-02-09', 'e': '2024-12-31', 'Cooper SE': '2024-03-03', 'EQ Fortwo': '2024-04-14', 'Silverado': '2024-06-30', 'Accord': '2025-06-21', 'Camry': '2024-04-12', 'Sonata': '2025-04-14', 'Explorer': '2025-10-23', 'Equinox': '2024-07-28', '3 Series': '2024-08-12', 'Q5': '2025-05-29', 'E-Class': '2025-07-17', 'Model S': '2024-03-21', 'Murano': '2024-11-04', 'XE': '2025-01-30'}

data_de_inspecao = {'A4': '2025-05-13', 'F-PACE': '2025-03-13', 'Vespa GTS 300': '2025-04-05', 'Ranger': '2024-07-18', 'Leaf': '2024-02-22', 'Cooper SE': '2025-12-24', 'F-Pace': '2024-05-25', 'Corolla': '2024-03-11', 'Civic': '2025-11-25', 'Mustang': '2024-08-02', 'Camaro': '2025-04-21', 'X5': '2025-05-28', 'C-Class': '2025-05-20', 'Altima': '2024-08-12', 'CX-5': '2025-08-25', 'Outback': '2024-10-11', 'Elantra': '2024-08-08', 'Soul': '2025-02-16', 'Wrangler': '2025-04-21', 'Discovery': '2025-01-20', 'XC90': '2025-03-27', 'Model 3': '2024-10-30', '911': '2025-02-03', 'Roma': '2025-03-20', 'Huracán': '2025-08-20', '720S': '2025-10-17', 'Panigale V4': '2024-04-07', 'Street Glide': '2025-10-16', 'R1250GS': '2025-04-09', 'YZF-R1': '2025-02-03', '1290 Super Duke R': '2024-07-16', 'CBR1000RR': '2025-04-07', 'Hayabusa': '2024-06-25', 'Street Triple': '2025-09-23', 'Ninja ZX-10R': '2024-03-22', 'RSV4': '2024-12-11', 'Brutale 1000 RR': '2024-09-07', 'Tahoe': '2024-03-08', '1500': '2024-12-24', 'F-150': '2026-01-15', 'Tacoma': '2024-05-29', 'Frontier': '2025-02-27', 'Land Cruiser': '2025-11-26', 'Chiron': '2024-06-09', 'Jesko': '2024-07-04', 'e': '2024-11-18', 'EQ Fortwo': '2024-02-15', 'Silverado': '2024-07-21', 'Accord': '2024-06-19', 'Camry': '2025-10-30', 'Sonata': '2025-04-24', 'Explorer': '2025-12-19', 'Equinox': '2025-06-16', '3 Series': '2025-11-10', 'Q5': '2025-01-26', 'E-Class': '2025-01-21', 'XE': '2024-11-02'}

# Step 2: Connect to the SQLite database
db_path = "./instance/luxuryrentals.db"  # Replace with your database file path
conn = sqlite3.connect(db_path)
# cursor = conn.cursor()

# cursor.execute("ALTER TABLE VEICULOS RENAME COLUMN Description TO desc_rapida")

# conn.commit()
# conn.close()


# Step 3: Load the existing table into a pandas DataFrame
table_name = "veiculos"  # Replace with the name of your table
df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)

# Step 4: Add the "Description" column using the dictionary
df["data_de_inspecao"] = df["modelo"].map(data_de_inspecao)

# Step 5: Write the updated DataFrame back to the SQLite database
df.to_sql(table_name, conn, if_exists="replace", index=False)

# Close the database connection
conn.close()

print("Database updated successfully!")

# keyslist = list(desc_detalhada.keys())
# print(keyslist)

# <!-- 
#   <div class="card p-3">
#     <div class="row g-0">
#       <div class="col-md-4">
#         <img
#           src="{{ url_for('views.get_vehicle_image', vehicle_id=vehicle.id) }}"
#           class="img-fluid rounded-start mt-4"
#           alt="..."
#         />
#       </div>
#       <div class="col-md-8">
#         <div class="card-body">
#           <h5 class="card-title">{{ vehicle.marca }} <span style="font-weight: 400;" >{{ vehicle.modelo }}</span></h5>
#           <p style="font-weight: 500;" class="card-text">{{ vehicle.desc_rapida }}</p>
#         </div>
#       </div>
#     </div>
#   </div> -->

#   <!-- <div class="card text-bg-light">
    

#         <img
#           src="{{ url_for('views.get_vehicle_image', vehicle_id=vehicle.id) }}"
#           class="card-img img-fluid"
#           alt="..."
#         />

#     <div class="card-img-overlay">
#       <h5 class="card-title">{{ vehicle.marca }} <span style="font-weight: 400;" >{{ vehicle.modelo }}</span></h5>
#       <p class="card-text">{{ desc_rapida }}</p>
#     </div>



#   </div>
#  -->

