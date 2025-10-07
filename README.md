# DermiDetect - Skin Cancer Classification System

![DermiDetect](static/image/DermiDetect.png)

A Flask-based web application for skin cancer classification using deep learning. The system uses a trained Convolutional Neural Network (CNN) to analyze skin lesion images and classify them into different categories.

## Features

- **Image Upload & Analysis**: Upload skin lesion images for automated classification
- **Multi-Class Classification**: Detects 8 different types of skin conditions:
  - Actinic keratoses and intraepithelial carcinomae
  - Basal Cell Carcinoma
  - Benign Keratosis
  - Dermatofibroma
  - Melanocytic nevus
  - Vascular Lesion
  - Melanoma
  - No Cancer Detected

- **Educational Resources**: Learn about different types of skin cancer
- **Responsive Design**: Works on desktop and mobile devices

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Machine Learning**: TensorFlow/Keras
- **Image Processing**: Pillow (PIL)
- **Frontend**: Bootstrap, HTML5, CSS3, JavaScript

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- Git

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/mysite.git
cd mysite
```

### 2. Create Virtual Environment

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the example environment file and update it with your settings:

```bash
cp .env.example .env
```

Edit `.env` file and set your configuration:

```env
SECRET_KEY=your-super-secret-key-here
DEBUG=True
PORT=2500
HOST=0.0.0.0
IMAGE_UPLOADS=static/image
MODEL_PATH=SkinCancerClassificationModelFinal.h5
```

**Important**: Generate a strong secret key for production:
```bash
python -c "import os; print(os.urandom(24).hex())"
```

### 5. Download the Model

The trained model file (`SkinCancerClassificationModelFinal.h5`) should be placed in the project root directory. 

**Note**: Due to file size limitations, the model file is not included in the repository. Please:
- Download it from [Google Drive/Dropbox link] (if applicable)
- Or train your own model using the training scripts

### 6. Run the Application

**Development Mode:**
```bash
python app.py
```

The application will be available at `http://localhost:2500`

**Production Mode (using Gunicorn):**
```bash
gunicorn app:app --bind 0.0.0.0:2500
```

## Project Structure

```
mysite/
├── app.py                          # Main Flask application
├── config.py                       # Configuration settings
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variables template
├── .gitignore                      # Git ignore rules
├── Procfile                        # Heroku deployment config
├── static/                         # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── image/                      # User uploaded images (ignored by git)
├── templates/                      # HTML templates
│   ├── forms/
│   │   ├── index.html
│   │   ├── try_now.html
│   │   ├── learn.html
│   │   └── q2_new.html
│   └── errors/
│       ├── 404.html
│       └── 500.html
└── SkinCancerClassificationModelFinal.h5  # Trained model (not in git)
```

## Usage

1. **Home Page**: Navigate to the home page to learn about the application
2. **Try Now**: Click "Try Now" to access the image upload interface
3. **Upload Image**: Select a skin lesion image (JPG, PNG format recommended)
4. **Get Results**: View the classification results and confidence scores
5. **Learn More**: Access the "Learn" section for educational content about skin cancer

## API Endpoints

- `GET /` or `/home` - Home page
- `GET /try_now` - Image upload page
- `POST /q2` - Image classification endpoint
- `GET /learn` - Educational resources
- `GET /q2/<filename>` - Display uploaded image

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Flask secret key for sessions | `dev-secret-key-change-in-production` |
| `DEBUG` | Enable debug mode | `True` |
| `PORT` | Application port | `2500` |
| `HOST` | Application host | `0.0.0.0` |
| `IMAGE_UPLOADS` | Upload directory path | `static/image` |
| `MODEL_PATH` | Model file path | `SkinCancerClassificationModelFinal.h5` |
| `IMG_WIDTH` | Image width for model | `28` |
| `IMG_HEIGHT` | Image height for model | `28` |
| `BATCH_SIZE` | Prediction batch size | `10` |

## Deployment

### Heroku Deployment

1. Install Heroku CLI
2. Login to Heroku:
   ```bash
   heroku login
   ```

3. Create a new Heroku app:
   ```bash
   heroku create your-app-name
   ```

4. Set environment variables:
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   ```

5. Deploy:
   ```bash
   git push heroku main
   ```

**Note**: Due to the large size of the model file, you may need to use Git LFS or upload it separately.

### Other Platforms

The application can be deployed to:
- AWS EC2/Elastic Beanstalk
- Google Cloud Platform
- Azure App Service
- DigitalOcean

Make sure to:
- Set `DEBUG=False` in production
- Use a strong `SECRET_KEY`
- Configure HTTPS
- Set up proper error logging

## Security Considerations

⚠️ **Important Security Notes:**

1. **Never commit `.env` file** - It contains sensitive information
2. **Use strong SECRET_KEY** - Generate a random key for production
3. **Disable DEBUG mode** - Set `DEBUG=False` in production
4. **Validate file uploads** - The app should validate file types and sizes
5. **HTTPS in production** - Always use HTTPS for production deployments

## Model Information

- **Input Size**: 28x28 pixels (RGB)
- **Architecture**: Custom CNN
- **Training Dataset**: [Specify your dataset]
- **Accuracy**: [Specify accuracy metrics if available]

## Troubleshooting

### Common Issues

**Import Errors:**
```bash
pip install --upgrade -r requirements.txt
```

**Model Not Found:**
- Ensure `SkinCancerClassificationModelFinal.h5` is in the project root
- Check the `MODEL_PATH` in `.env`

**Upload Directory Error:**
- The app automatically creates `static/image` directory
- Ensure write permissions

**Port Already in Use:**
- Change `PORT` in `.env` to a different value
- Or stop the process using the port

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

⚠️ **Medical Disclaimer**: This application is for educational and research purposes only. It is NOT a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified health providers with any questions regarding medical conditions.

## Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/mysite](https://github.com/yourusername/mysite)

## Acknowledgments

- [TensorFlow](https://www.tensorflow.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)
- Dataset source: [Specify if applicable]
