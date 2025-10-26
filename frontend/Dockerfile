# ---------- Build Stage ----------
FROM node:20-alpine AS builder

# Install pnpm globally
RUN npm install -g pnpm

WORKDIR /app

# Copy package files
COPY package.json pnpm-lock.yaml ./

# Install dependencies using pnpm
RUN pnpm install --frozen-lockfile

# Copy the rest of your source code
COPY . .

# Build Next.js app
RUN pnpm build

# ---------- Run Stage ----------
FROM node:20-alpine AS runner

# Install pnpm globally again
RUN npm install -g pnpm

WORKDIR /app

# Copy build output and dependencies
COPY --from=builder /app ./

EXPOSE 3000

# Run production server
CMD ["pnpm", "start"]

