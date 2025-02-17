import abc

from pydantic import AwareDatetime, NonNegativeFloat

from pyrb.models.portfolio import PortfolioReturn
from pyrb.models.position import Position


class Portfolio(abc.ABC):
    @property
    @abc.abstractmethod
    def total_value(self) -> NonNegativeFloat:
        """Calculates the total value of the portfolio.
        total value = cash + sum of the market value of all positions

        Returns:
            NonNegativeFloat: The total value of the portfolio.
        """
        ...

    @property
    @abc.abstractmethod
    def cash_balance(self) -> NonNegativeFloat:
        """Returns the cash balance of the portfolio.

        Returns:
            NonNegativeFloat: The cash balance of the portfolio.
        """
        ...

    @property
    @abc.abstractmethod
    def positions(self) -> list[Position]:
        """Returns a list of all positions in the portfolio.

        Returns:
            list[Position]: A list of all positions in the portfolio.
        """
        ...

    @property
    @abc.abstractmethod
    def holding_symbols(self) -> list[str]:
        """Returns a list of symbols for all positions in the portfolio.

        Returns:
            list[str]: A list of symbols for all positions in the portfolio.
        """
        ...

    @abc.abstractmethod
    def get_position(self, symbol: str) -> Position | None:
        """Returns the position object for the given symbol.

        Args:
            symbol : The symbol of the position to retrieve.

        Returns:
            Position | None: The position object for the given symbol,
                             if the symbol is not found, None will be returned.
        """
        ...

    @abc.abstractmethod
    def get_position_amount(self, symbol: str) -> NonNegativeFloat:
        """Returns the total amount of the position for the given symbol.
        If the symbol is not found, 0 will be returned.

        Args:
            symbol : The symbol of the position to retrieve.

        Returns:
            NonNegativeFloat: The total amount of the position for the given symbol.
        """
        ...

    @abc.abstractmethod
    def fetch_returns(
        self, start_dt: AwareDatetime, end_dt: AwareDatetime
    ) -> list[PortfolioReturn]:
        """Fetches the returns of the portfolio for the given period.

        Args:
            start_dt (AwareDatetime): The start date of the period.
            end_dt (AwareDatetime): The end date of the period.

        Returns:
            list[PortfolioReturn]: A list of PortfolioReturn objects.
        """
        ...

    @abc.abstractmethod
    def refresh(self) -> None:
        """Refreshes the portfolio object."""
        ...
