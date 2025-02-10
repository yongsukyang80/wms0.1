from app import create_app, db
from app.models.models import User, Product, Location, Inventory
import random

app = create_app()

def init_db():
    with app.app_context():
        # 데이터베이스 테이블 생성
        db.create_all()

        # 관리자 계정 생성
        admin = User(
            username='admin',
            password='admin123',  # 실제 운영시에는 반드시 해시처리 필요
            email='admin@example.com',
            role='admin'
        )
        db.session.add(admin)

        # 로케이션 생성
        zones = ['보관존', '피킹존', '불량존', '자동화존']
        for zone in zones:
            for i in range(10):
                location = Location(
                    location_code=f'{zone[0]}{i+1:03d}',
                    zone_type=zone
                )
                db.session.add(location)

        db.session.commit()

if __name__ == '__main__':
    init_db() 