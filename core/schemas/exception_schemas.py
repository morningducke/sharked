from fastapi import status, HTTPException

UnauthorizedException = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

UserAreadyExistsException = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")