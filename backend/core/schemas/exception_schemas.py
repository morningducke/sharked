from fastapi import status, HTTPException

UnauthorizedException = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

UserAreadyExistsException = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
UserNotFound = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")
ForbiddenAccess = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficent rights")