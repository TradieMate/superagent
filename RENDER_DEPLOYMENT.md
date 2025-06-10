# Superagent Render Deployment Guide

This guide provides step-by-step instructions to deploy Superagent on Render with proper port binding configuration using Docker.

## Issues Fixed

The following port binding issues have been resolved:

1. **Backend (FastAPI)**: Fixed gunicorn to bind to `0.0.0.0:$PORT` instead of `:$PORT`
2. **Frontend (Next.js)**: Configured to use PORT environment variable and bind to `0.0.0.0`
3. **Health Check**: Added `/health` endpoint for Render's health checks
4. **Startup Script**: Created robust startup script with proper error handling

## Docker-Based Deployment

### Backend API Deployment

1. **Create Web Service**:
   - Go to [Render Dashboard](https://dashboard.render.com/create?type=web)
   - Select "Build and deploy from a Git repository"
   - Choose your Superagent fork

2. **Configure Service**:
   - **Name**: `superagent-api`
   - **Root Directory**: `./libs/superagent`
   - **Environment**: `Docker`
   - **Dockerfile Path**: `Dockerfile`
   - **Plan**: Starter or higher

3. **Environment Variables**:
   ```
   OPENAI_API_KEY=your_openai_key
   DATABASE_URL=your_database_url
   DATABASE_MIGRATION_URL=your_migration_url
   JWT_SECRET=your_jwt_secret
   MEMORY=motorhead
   MEMORY_API_URL=https://memory.superagent.sh
   VECTORSTORE=pinecone
   SUPERAGENT_API_URL=https://your-api-service.onrender.com
   ```
   
   > **Note**: Render automatically sets the `PORT` environment variable to `10000`. The Dockerfile is configured to use this automatically.

### Frontend UI Deployment

1. **Create Web Service**:
   - Create another web service for the frontend
   - **Name**: `superagent-ui`
   - **Root Directory**: `./libs/ui`
   - **Environment**: `Docker`
   - **Dockerfile Path**: `Dockerfile`

2. **Environment Variables**:
   ```
   NODE_ENV=production
   NEXT_PUBLIC_SUPERAGENT_API_URL=https://your-api-service.onrender.com
   NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
   NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_key
   ```
   
   > **Note**: Render automatically sets the `PORT` environment variable. The Dockerfile is configured to use this automatically.

## Required Environment Variables

### Backend (Mandatory)
- `OPENAI_API_KEY`: Your OpenAI API key
- `DATABASE_URL`: PostgreSQL database connection string
- `DATABASE_MIGRATION_URL`: Database URL for migrations
- `JWT_SECRET`: Secret key for JWT tokens

### Backend (Optional but Recommended)
- `MEMORY`: Memory provider (default: motorhead)
- `VECTORSTORE`: Vector database provider (pinecone, qdrant, weaviate)
- `REDIS_MEMORY_URL`: Redis connection for memory storage
- `PINECONE_API_KEY`, `PINECONE_ENVIRONMENT`, `PINECONE_INDEX`: For Pinecone vector store

### Frontend
- `NEXT_PUBLIC_SUPERAGENT_API_URL`: URL of your deployed backend API
- `NEXT_PUBLIC_SUPABASE_URL`: Supabase project URL
- `NEXT_PUBLIC_SUPABASE_ANON_KEY`: Supabase anonymous key

> **Important**: Do not manually set the `PORT` environment variable. Render automatically provides this and the Dockerfiles are configured to use it.

## Health Checks

The backend now includes a health check endpoint at `/health` that returns:
```json
{
  "status": "healthy",
  "service": "superagent-api"
}
```

## Troubleshooting

### Port Binding Issues
- Render automatically sets the `PORT` environment variable (usually `10000`)
- The application now properly binds to `0.0.0.0:$PORT`
- Do not manually override the `PORT` variable

### Worker Termination (Signal 9)
- Increase memory allocation in Render plan
- Reduce number of workers if needed (set `WORKERS` environment variable)
- Increase timeout (set `TIMEOUT` environment variable)

### Database Connection Issues
- Ensure `DATABASE_URL` is correctly formatted
- Check that your database allows connections from Render's IP ranges
- Verify database credentials and permissions

### Startup Delays
- The startup script now includes proper initialization steps
- Database migrations run automatically on startup
- Prisma client is generated during the build process

## Monitoring

- Use Render's built-in logs to monitor application startup
- Health check endpoint provides service status
- Monitor resource usage in Render dashboard

## Support

For additional support:
- Check Render's documentation: https://render.com/docs
- Review Superagent documentation
- Check application logs in Render dashboard